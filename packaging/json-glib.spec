%bcond_with introspection

Name:           json-glib
Version:        0.16.0
Release:        0
License:        LGPL-2.1+
Summary:        Library for JavaScript Object Notation format
Url:            http://live.gnome.org/JsonGlib
Group:          Development/Libraries/C and C++
Source0:        http://download.gnome.org/sources/json-glib/0.15/%{name}-%{version}.tar.xz
Source99:       baselibs.conf
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
Group:          Development/Libraries/C and C++
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
Group:          Development/Libraries/C and C++
Requires:       libjson-glib = %{version}
%if %{with introspection}
Requires:       typelib-Json = %{version}
%endif

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

%build
%configure
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name}-1.0

mv %{name}-1.0.lang %{name}.lang

%post -n libjson-glib -p /sbin/ldconfig

%postun -n libjson-glib -p /sbin/ldconfig

%files -n libjson-glib
%defattr(-,root,root)
%license COPYING
%{_libdir}/*.so.*

%if %{with introspection}
%files -n typelib-Json
%defattr(-,root,root)
%{_libdir}/girepository-1.0/Json-1.0.typelib
%endif

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}-1.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%if %{with introspection}
%{_datadir}/gir-1.0/*.gir
%endif
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/%{name}


%changelog
