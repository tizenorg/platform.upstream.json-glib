%bcond_with introspection

%define run_tests 0
%if %{run_tests}
    # check is defined off at .rpmmacros file.
    %undefine check
%endif

Name:           json-glib
Version:        1.1.1
Release:        0
License:        LGPL-2.1
Summary:        Library for JavaScript Object Notation format
Url:            http://live.gnome.org/JsonGlib
Group:          System/Libraries
#X-Vcs-Url:     git://git.gnome.org/json-glib
Source0:        http://download.gnome.org/sources/json-glib/%{version}/%{name}-%{version}.tar.xz
Source99:       baselibs.conf
Source1001: 	json-glib.manifest
%if %{with introspection}
BuildRequires:  gobject-introspection-devel
%endif
BuildRequires:  pkgconfig(glib-2.0)

%description
JSON is a lightweight data-interchange format.It is easy for humans to
read and write. It is easy for machines to parse and generate.

JSON-GLib provides a parser and a generator GObject classes and various
wrappers for the complex data types employed by JSON, such as arrays
and objects.

JSON-GLib uses GLib native data types and the generic value container
GValue for ease of development. It also provides integration with the
GObject classes for direct serialization into, and deserialization from,
JSON data streams.

%package -n libjson-glib
Summary:        Library for JavaScript Object Notation format
Group:          System/Libraries
# To make lang subpackage installable
Provides:       %{name} = %{version}

%description -n libjson-glib
JSON is a lightweight data-interchange format.It is easy for humans to
read and write. It is easy for machines to parse and generate.

JSON-GLib provides a parser and a generator GObject classes and various
wrappers for the complex data types employed by JSON, such as arrays
and objects.

JSON-GLib uses GLib native data types and the generic value container
GValue for ease of development. It also provides integration with the
GObject classes for direct serialization into, and deserialization from,
JSON data streams.

%package -n typelib-Json
Summary:        Library for JavaScript Object Notation format -- Introspection bindings
Group:          System/Libraries

%description -n typelib-Json
JSON is a lightweight data-interchange format.It is easy for humans to
read and write. It is easy for machines to parse and generate.

JSON-GLib provides a parser and a generator GObject classes and various
wrappers for the complex data types employed by JSON, such as arrays
and objects.

JSON-GLib uses GLib native data types and the generic value container
GValue for ease of development. It also provides integration with the
GObject classes for direct serialization into, and deserialization from,
JSON data streams.

This package provides the GObject Introspection bindings for JSON-GLib.

%package devel
Summary:        Library for JavaScript Object Notation format - Development Files
Group:          System/Libraries
Requires:       libjson-glib = %{version}
%if %{with introspection}
Requires:       typelib-Json = %{version}
%endif
BuildRequires:	gettext
BuildRequires:	gtk-doc

%description devel
JSON is a lightweight data-interchange format.It is easy for humans to
read and write. It is easy for machines to parse and generate.

JSON-GLib provides a parser and a generator GObject classes and various
wrappers for the complex data types employed by JSON, such as arrays
and objects.

JSON-GLib uses GLib native data types and the generic value container
GValue for ease of development. It also provides integration with the
GObject classes for direct serialization into, and deserialization from,
JSON data streams.

This package contains development files needed to develop with the
json-glib library.

%lang_package
%prep
%setup -q
cp %{SOURCE1001} .

%build
NOCONFIGURE=1
%autogen
%reconfigure --disable-man
make %{?_smp_mflags}

%check
%if %{run_tests}
    %__make check || exit 0
%endif

%install
%make_install
%find_lang %{name}-1.0

mv %{name}-1.0.lang %{name}.lang

%post -n libjson-glib -p /sbin/ldconfig

%postun -n libjson-glib -p /sbin/ldconfig

%files -n libjson-glib
%manifest %{name}.manifest
%defattr(-,root,root)
%license COPYING
%{_libdir}/*.so.*
%{_bindir}/*

%if %{with introspection}
%files -n typelib-Json
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/girepository-1.0/Json-1.0.typelib
%endif

%files devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_includedir}/%{name}-1.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%if %{with introspection}
%{_datadir}/gir-1.0/*.gir
%endif

%changelog
