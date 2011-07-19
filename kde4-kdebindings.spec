#
# Conditional build:
%bcond_with	dotnet	# build without dotnet bindings
%bcond_without	smoke	# build libsmokekde
%bcond_with	ruby	# build ruby bindings

%define		_state		stable
%define		orgname		kdebindings
%define		qtver		4.7.3
%define		sipver		2:4.12
%define		pyqtver		4.8.2-3

Summary:	KDE bindings to non-C++ languages
Summary(pl.UTF-8):	Dowiązania KDE dla języków innych niż C++
Name:		kde4-kdebindings
Version:	4.6.5
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	c16e25613296edd82819b6e490360201
Patch100:	%{name}-branch.diff
Patch1:		%{name}-hack.patch
BuildRequires:	PolicyKit-devel
BuildRequires:	akonadi-devel
BuildRequires:	attica-devel
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	gdbm-devel
BuildRequires:	kde4-kdebase-workspace-devel >= %{version}
# for libsmokeokular
BuildRequires:	kde4-kdegraphics-devel >= %{version}
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-kdepimlibs-devel >= %{version}
%{?with_dotnet:BuildRequires:	mono-csharp}
%{?with_dotnet:BuildRequires:	monodoc}
BuildRequires:	perl-devel
BuildRequires:	phonon-devel >= 4.4.1
BuildRequires:	pkgconfig
BuildRequires:	polkit-qt-gui-devel >= 0.9.3
# PolicyKit-kde (qt)
BuildRequires:	python-PyQt4-devel >= %{pyqtver}
BuildRequires:	python-sip >= %{sipver}
BuildRequires:	qimageblitz-devel
BuildRequires:	qscintilla2-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	qwt-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.600
%if %{with ruby}
BuildRequires:	ruby-devel
%{?with_smoke:BuildRequires:	ruby-qt4-devel >= 2.1.0}
%endif
BuildRequires:	shared-desktop-ontologies-devel
BuildRequires:	soprano-devel >= 2.4.64
#BuildConflicts:	qt-devel
%{!?with_smoke:BuildConflicts:	ruby-qt4-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bindings for the K Desktop Environment: provide interfaces to many
diferent programming languages to use KDE native resources and
widgets.

%description -l pl.UTF-8
Dowiązania KDE/qt dla języków innych niż C++ pozwalające używać
natywnych dla KDE zasobów i widgetów.

%package kimono
Summary:	C# Mono KDE4 bindings
Summary(pl.UTF-8):	Dowiązania C# Mono do KDE4
Group:		X11/Libraries

%description kimono
C# Mono KDE4 bindings.

%description kimono -l pl.UTF-8
Dowiązania C# Mono do KDE4.

%package -n qyoto
Summary:	C# Mono Qt4 bindings
Summary(pl.UTF-8):	Dowiązania C# Mono dla Qt4
Group:		X11/Libraries

%description -n qyoto
C# Mono Qt4 bindings.

%description -n qyoto -l pl.UTF-8
Dowiązania C# Mono dla Qt4.

%package -n qyoto-devel
Summary:	qyoto header files
Summary(pl.UTF-8):	Pliki nagłówkowe dla qyoto
Group:		X11/Development/Libraries
Requires:	qyoto = %{version}-%{release}

%description -n qyoto-devel
qyoto header files.

%description -n qyoto-devel -l pl.UTF-8
Pliki nagłówkowe dla qyoto.

%package ruby-qt
Summary:	Qt bindings for Ruby
Summary(pl.UTF-8):	Dowiązania Qt dla języka Ruby
Group:		X11/Libraries

%description ruby-qt
A Qt bindings for Ruby using the SMOKE technology.

%description ruby-qt -l pl.UTF-8
Dowiązania Qt dla języka Ruby przy użyciu technologii SMOKE.

%package ruby-kde
Summary:	KDE bindings for Ruby
Summary(pl.UTF-8):	Dowiązania KDE dla języka Ruby
Group:		X11/Libraries

%description ruby-kde
A KDE bindings for Ruby using the SMOKE technology.

%description ruby-kde -l pl.UTF-8
Dowiązania KDE dla języka Ruby przy użyciu technologii SMOKE.

%package ruby-devel
Summary:	KDE header files for Ruby
Summary(pl.UTF-8):	Pliki nagłówkowe KDE dla języka Ruby
Group:		X11/Development/Libraries
Requires:	%{name}-ruby-qt = %{version}-%{release}

%description ruby-devel
KDE header files for Ruby.

%description ruby-devel -l pl.UTF-8
Pliki nagłówkowe KDE dla języka Ruby.

%package perl-devel
Summary:	KDE bindings for Perl 
Summary(pl.UTF-8):	Dowiązania KDE dla Perla
Group:		Development/Languages/perl

%description perl-devel
KDE bindings for Perl.

%description perl-devel -l pl.UTF-8
Dowiązania KDE dla Perla.

%package smoke-qt
Summary:	A SMOKE library for Qt
Summary(pl.UTF-8):	Biblioteka SMOKE dla Qt
Group:		X11/Libraries

%description smoke-qt
SMOKE library (Scripting Meta Object Kompiler Engine) dla Qt.

%description smoke-qt -l pl.UTF-8
Biblioteka SMOKE (Scripting Meta Object Kompiler Engine - silnik
kompilatora metaobiektów skryptowych) dla Qt.

%package smoke-kde
Summary:	A SMOKE library for KDE 4
Summary(pl.UTF-8):	Biblioteka SMOKE dla KDE 4
Group:		X11/Libraries

%description smoke-kde
SMOKE library (Scripting Meta Object Kompiler Engine) dla KDE 4.

%description smoke-kde -l pl.UTF-8
Biblioteka SMOKE (Scripting Meta Object Kompiler Engine - silnik
kompilatora metaobiektów skryptowych) dla KDE 4.

%package smoke-devel
Summary:	Header files for SMOKE libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek SMOKE
Group:		X11/Development/Libraries
Requires:	%{name}-smoke-kde = %{version}-%{release}
Requires:	%{name}-smoke-qt = %{version}-%{release}

%description smoke-devel
Header files for SMOKE libraries.

%description smoke-devel -l pl.UTF-8
Pliki nagłówkowe bibliotek SMOKE.

%package -n python-PyKDE4
Summary:	PyKDE4 - Python bindings for KDE 4
Summary(pl.UTF-8):	PyKDE4 - dowiązania KDE 4 dla Pythona
Group:		Libraries/Python
Requires:	python-PyQt4 >= %{pyqtver}
Requires:	python-sip >= %{sipver}

%description -n python-PyKDE4
PyKDE4 is a set of Python bindings for the KDE 4 desktop environment.
The bindings are implemented as a set of Python modules, which
correspond to KDE libraries.

%description -n python-PyKDE4 -l pl.UTF-8
PyKDE4 to zbiór dowiązań środowiska graficznego KDE 4 dla Pythona.
Dowiązania są zaimplementowane jako zbiór modułów Pythona
odpowiadających poszczególnym bibliotekom KDE.

%package -n python-PyKDE4-devel
Summary:	SIP development files for PyKDE4
Summary(pl.UTF-8):	Pliki programistyczne SIP dla PyKDE4
Group:		Development/Languages/Python
Requires:	python-PyKDE4 = %{version}-%{release}
Requires:	python-PyQt4-devel >= %{pyqtver}
Requires:	python-sip-devel >= %{sipver}

%description -n python-PyKDE4-devel
SIP development files for PyKDE4, needed to build other bindings for
C++ classes that inherit from any of the KDE4 classes.

%description -n python-PyKDE4-devel -l pl.UTF-8
Pliki programistyczne SIP dla PyKDE4, potrzebne do budowania innych
dowiązań do klas C++ dziedziczących z dowolnej klasy KDE4.

%package -n python-PyKDE4-devel-tools
Summary:	PyKDE4 development tools
Summary(pl.UTF-8):	Narzędzia programistyczne PyKDE4
Group:		Development/Languages/Python
Requires:	python-PyKDE4 = %{version}-%{release}
Requires:	python-PyQt4-devel-tools >= %{pyqtver}

%description -n python-PyKDE4-devel-tools
PyKDE4 development tool: pykdeuic4.

%description -n python-PyKDE4-devel-tools -l pl.UTF-8
Narzędzie programistyczne PyKDE4: pykdeuic4.

%package -n python-PyKDE4-examples
Summary:	PyKDE4 examples
Summary(pl.UTF-8):	Przykłady dla PyKDE4
Group:		Libraries/Python

%description -n python-PyKDE4-examples
PyKDE4 examples.

%description -n python-PyKDE4-examples -l pl.UTF-8
Przykłady dla PyKDE4.

%prep
%setup -q -n %{orgname}-%{version}
#%patch100 -p0
%patch1 -p1
# Very ugly hack, but damn, i'm sick of this package
%if %{without smoke}
%{__sed} -i -e 's/macro_optional_add_subdirectory(smoke)//' CMakeLists.txt
%endif
%if %{without ruby}
%{__sed} -i -e 's/macro_optional_add_subdirectory(ruby)//' CMakeLists.txt
%endif
%if %{without csharp}
%{__sed} -i -e 's/macro_optional_add_subdirectory(csharp)//' CMakeLists.txt
%{__sed} -i -e 's/macro_optional_add_subdirectory(java)//' CMakeLists.txt
%{__sed} -i -e 's/macro_optional_add_subdirectory(php)//' CMakeLists.txt
%{__sed} -i -e 's/macro_optional_add_subdirectory(falcon)//' CMakeLists.txt
%endif

%build
install -d build
cd build
%cmake \
	-DBUILD_smoke=%{!?with_smoke:OFF}%{?with_smoke:ON} \
	-DBUILD_ruby=%{!?with_ruby:OFF}%{?with_ruby:ON} \
	-DCUSTOM_PERL_SITE_ARCH_DIR=%{perl_vendorarch} \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/python-PyKDE4-%{version}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

mv $RPM_BUILD_ROOT%{_datadir}/apps/pykde4/examples/* $RPM_BUILD_ROOT%{_examplesdir}/python-PyKDE4-%{version}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}/PyKDE4
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}/PyKDE4

# don't use py_postclean
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/PyKDE4/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%post	kimono -p /sbin/ldconfig
%postun	kimono -p /sbin/ldconfig

%post	-n qyoto -p /sbin/ldconfig
%postun	-n qyoto -p /sbin/ldconfig

%post	smoke-qt -p /sbin/ldconfig
%postun	smoke-qt -p /sbin/ldconfig

%post	smoke-kde -p /sbin/ldconfig
%postun	smoke-kde -p /sbin/ldconfig

%post	ruby-qt -p /sbin/ldconfig
%postun	ruby-qt -p /sbin/ldconfig

%if %{with dotnet}
%files kimono
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kimonopluginfactory.so
%attr(755,root,root) %{_libdir}/libakonadi-sharp.so
%attr(755,root,root) %{_libdir}/libkhtml-sharp.so
%attr(755,root,root) %{_libdir}/libkimono.so
%attr(755,root,root) %{_libdir}/libktexteditor-sharp.so
%attr(755,root,root) %{_libdir}/libnepomuk-sharp.so
%attr(755,root,root) %{_libdir}/libplasma-sharp.so
%attr(755,root,root) %{_libdir}/libsoprano-sharp.so
%{_prefix}/lib/mono/2.0/akonadi.dll
%{_prefix}/lib/mono/2.0/kde-dotnet.dll
%{_prefix}/lib/mono/2.0/khtml-dll.dll
%{_prefix}/lib/mono/2.0/ktexteditor-dotnet.dll
%{_prefix}/lib/mono/2.0/nepomuk-dll.dll
%{_prefix}/lib/mono/2.0/plasma-dll.dll
%{_prefix}/lib/mono/2.0/soprano.dll
%{_prefix}/lib/mono/gac/akonadi
%{_prefix}/lib/mono/gac/kde-dotnet
%{_prefix}/lib/mono/gac/khtml-dll
%{_prefix}/lib/mono/gac/ktexteditor-dotnet
%{_prefix}/lib/mono/gac/nepomuk-dll
%{_prefix}/lib/mono/gac/plasma-dll
%{_prefix}/lib/mono/gac/soprano
%dir %{_datadir}/apps/plasma_scriptengine_kimono
%{_datadir}/apps/plasma_scriptengine_kimono/PlasmaScriptengineKimono.dll
%{_datadir}/kde4/services/plasma-scriptengine-kimono-applet.desktop
%{_datadir}/kde4/services/plasma-scriptengine-kimono-dataengine.desktop

%files -n qyoto
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqyoto.so
%attr(755,root,root) %ghost %{_libdir}/libqyotoshared.so.?
%attr(755,root,root) %{_libdir}/libqyotoshared.so.*.*.*
%attr(755,root,root) %{_libdir}/libqtscript-sharp.so
%attr(755,root,root) %{_libdir}/libqttest-sharp.so
%attr(755,root,root) %{_libdir}/libqtuitools-sharp.so
%attr(755,root,root) %{_libdir}/libqtwebkit-sharp.so
%attr(755,root,root) %{_libdir}/libqimageblitz-sharp.so
%{_prefix}/lib/mono/2.0/qt-dotnet.dll
%{_prefix}/lib/mono/2.0/qtscript.dll
%{_prefix}/lib/mono/2.0/qttest.dll
%{_prefix}/lib/mono/2.0/qtuitools.dll
%{_prefix}/lib/mono/2.0/qtwebkit.dll
%{_prefix}/lib/mono/2.0/qimageblitz.dll
%{_prefix}/lib/mono/gac/qt-dotnet
%{_prefix}/lib/mono/gac/qtscript
%{_prefix}/lib/mono/gac/qttest
%{_prefix}/lib/mono/gac/qtuitools
%{_prefix}/lib/mono/gac/qtwebkit
%{_prefix}/lib/mono/gac/qimageblitz

%files -n qyoto-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/csrcc
%attr(755,root,root) %{_bindir}/uics
%attr(755,root,root) %{_libdir}/libqyotoshared.so
%{_includedir}/qyoto
%{_pkgconfigdir}/qyoto.pc
%{_pkgconfigdir}/qtscript-sharp.pc
%{_pkgconfigdir}/qttest-sharp.pc
%{_pkgconfigdir}/qtuitools-sharp.pc
%{_pkgconfigdir}/qtwebkit-sharp.pc
%endif

%if %{with smoke}
%files smoke-qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/smokeapi
%attr(755,root,root) %{_bindir}/puic4
%attr(755,root,root) %{_bindir}/smokegen
%attr(755,root,root) %{_libdir}/libsmokeqt*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokeqsci.so.?
%attr(755,root,root) %{_libdir}/libsmokeqsci.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokeqwt.so.?
%attr(755,root,root) %{_libdir}/libsmokeqwt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokeqt*.so.?
%attr(755,root,root) %{_libdir}/libsmokeqimageblitz.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokeqimageblitz.so.?
%attr(755,root,root) %ghost %{_libdir}/libsmokebase.so.?
%attr(755,root,root) %{_libdir}/libsmokebase.so.*.*.*
%dir %{_libdir}/smokegen
%attr(755,root,root) %{_libdir}/smokegen/generator_dump.so
%attr(755,root,root) %{_libdir}/smokegen/generator_smoke.so
%attr(755,root,root) %{_libdir}/libcppparser.so
%{_datadir}/smokegen

%files smoke-kde
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsmokeakonadi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokeakonadi.so.?
%attr(755,root,root) %{_libdir}/libsmokek*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokek*.so.?
%attr(755,root,root) %{_libdir}/libsmokenepomuk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokenepomuk.so.?
#%attr(755,root,root) %{_libdir}/libsmokephonon.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libsmokephonon.so.?
%attr(755,root,root) %{_libdir}/libsmokeplasma.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokeplasma.so.?
%attr(755,root,root) %{_libdir}/libsmokesolid.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokesolid.so.?
%attr(755,root,root) %{_libdir}/libsmokesoprano.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokesoprano.so.?
%attr(755,root,root) %{_libdir}/kde4/kperlpluginfactory.so
%attr(755,root,root) %ghost %{_libdir}/libsmokeattica.so.?
%attr(755,root,root) %{_libdir}/libsmokeattica.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokenepomukquery.so.?
%attr(755,root,root) %{_libdir}/libsmokenepomukquery.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokeokular.so.?
%attr(755,root,root) %{_libdir}/libsmokeokular.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokephonon.so.?
%attr(755,root,root) %{_libdir}/libsmokephonon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokesopranoclient.so.?
%attr(755,root,root) %{_libdir}/libsmokesopranoclient.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokesopranoserver.so.?
%attr(755,root,root) %{_libdir}/libsmokesopranoserver.so.*.*.*

%files smoke-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsmokeakonadi.so
%attr(755,root,root) %{_libdir}/libsmokeattica.so
%attr(755,root,root) %{_libdir}/libsmokeq*.so
%attr(755,root,root) %{_libdir}/libsmokek*.so
%attr(755,root,root) %{_libdir}/libsmokenepomuk.so
#%attr(755,root,root) %{_libdir}/libsmokephonon.so
%attr(755,root,root) %{_libdir}/libsmokeplasma.so
%attr(755,root,root) %{_libdir}/libsmokesolid.so
%attr(755,root,root) %{_libdir}/libsmokesoprano.so
%attr(755,root,root) %{_libdir}/libsmokenepomukquery.so
%attr(755,root,root) %{_libdir}/libsmokeokular.so
%attr(755,root,root) %{_libdir}/libsmokephonon.so
%attr(755,root,root) %{_libdir}/libsmokesopranoclient.so
%attr(755,root,root) %{_libdir}/libsmokesopranoserver.so
%attr(755,root,root) %{_libdir}/libsmokebase.so
%dir %{_includedir}/smoke
%{_includedir}/smoke/*.h
%{_includedir}/smoke.h
%{_includedir}/smokegen
%endif

%if %{with ruby}
%files ruby-qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rbqtapi
%attr(755,root,root) %{_bindir}/rbuic4
%attr(755,root,root) %{_bindir}/rbrcc
%attr(755,root,root) %{_libdir}/libqtruby4shared.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqtruby4shared.so.2
%attr(755,root,root) %{_libdir}/libsmokeokular.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokeokular.so.2
%{ruby_sitelibdir}/Qt.rb
%{ruby_sitelibdir}/Qt3.rb
%{ruby_sitelibdir}/Qt4.rb
%dir %{ruby_sitelibdir}/Qt
%{ruby_sitelibdir}/Qt/qtruby4.rb
%attr(755,root,root) %{ruby_sitearchdir}/qtruby4.so
%{ruby_sitelibdir}/Qt/active_item_model.rb
%{ruby_sitelibdir}/Qt/active_table_model.rb
%attr(755,root,root) %{ruby_sitearchdir}/okular.so
%dir %{ruby_sitelibdir}/okular
%{ruby_sitelibdir}/okular/okular.rb
%attr(755,root,root) %{ruby_sitearchdir}/qtwebkit.so
%dir %{ruby_sitelibdir}/qtwebkit
%{ruby_sitelibdir}/qtwebkit/qtwebkit.rb
%attr(755,root,root) %{ruby_sitearchdir}/qtuitools.so
%dir %{ruby_sitelibdir}/qtuitools
%{ruby_sitelibdir}/qtuitools/qtuitools.rb
%attr(755,root,root) %{ruby_sitearchdir}/qtscript.so
%dir %{ruby_sitelibdir}/qtscript
%{ruby_sitelibdir}/qtscript/qtscript.rb
%attr(755,root,root) %{ruby_sitearchdir}/qttest.so
%dir %{ruby_sitelibdir}/qttest
%{ruby_sitelibdir}/qttest/qttest.rb

%files ruby-kde
%defattr(644,root,root,755)
%attr(755,root,root) %{ruby_sitearchdir}/akonadi.so
%dir %{ruby_sitelibdir}/akonadi
%{ruby_sitelibdir}/akonadi/akonadi.rb
%attr(755,root,root) %{ruby_sitearchdir}/soprano.so
%dir %{ruby_sitelibdir}/soprano
%{ruby_sitelibdir}/soprano/soprano.rb
%{_desktopdir}/kde4/dbpedia_references.desktop
%dir %{_datadir}/apps/dbpedia_references
%{_datadir}/apps/dbpedia_references/dbpedia_references.rb
%attr(755,root,root) %{ruby_sitearchdir}/korundum4.so
%attr(755,root,root) %{_libdir}/kde4/krubypluginfactory.so
%attr(755,root,root) %{_bindir}/krubyapplication
%{ruby_sitelibdir}/KDE/korundum4.rb
%attr(755,root,root) %{_bindir}/rbkconfig_compiler4
%attr(755,root,root) %{ruby_sitearchdir}/khtml.so
%dir %{ruby_sitelibdir}/khtml
%{ruby_sitelibdir}/khtml/khtml.rb
%attr(755,root,root) %{ruby_sitearchdir}/ktexteditor.so
%dir %{ruby_sitelibdir}/ktexteditor
%{ruby_sitelibdir}/ktexteditor/ktexteditor.rb
%attr(755,root,root) %{ruby_sitearchdir}/nepomuk.so
%dir %{ruby_sitelibdir}/nepomuk
%{ruby_sitelibdir}/nepomuk/nepomuk.rb
%attr(755,root,root) %{ruby_sitearchdir}/plasma_applet.so
%dir %{ruby_sitelibdir}/KDE
%{ruby_sitelibdir}/KDE/plasma.rb
%attr(755,root,root) %{ruby_sitearchdir}/solid.so
%dir %{ruby_sitelibdir}/solid
%{ruby_sitelibdir}/solid/solid.rb
%attr(755,root,root) %{_libdir}/kde4/krossruby.so

%files ruby-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsmokeokular.so
%attr(755,root,root) %{_libdir}/libqtruby4shared.so
%dir %{_includedir}/qtruby
%{_includedir}/qtruby/*.h
%endif

%files perl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/prcc4_bin
%attr(755,root,root) %{_bindir}/qdbusxml2perl
%{perl_vendorarch}/*.pm
%{perl_vendorarch}/QtCore4
%dir %{perl_vendorarch}/auto/*
%attr(755,root,root) %{perl_vendorarch}/auto/*/*.so

%files -n python-PyKDE4
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kpythonpluginfactory.so
%attr(755,root,root) %{_libdir}/kde4/krosspython.so
%dir %{py_sitedir}/PyKDE4
%attr(755,root,root) %{py_sitedir}/PyKDE4/akonadi.so
%attr(755,root,root) %{py_sitedir}/PyKDE4/dnssd.so
%attr(755,root,root) %{py_sitedir}/PyKDE4/kdecore.so
%attr(755,root,root) %{py_sitedir}/PyKDE4/kdeui.so
%attr(755,root,root) %{py_sitedir}/PyKDE4/khtml.so
%attr(755,root,root) %{py_sitedir}/PyKDE4/kio.so
%attr(755,root,root) %{py_sitedir}/PyKDE4/knewstuff.so
%attr(755,root,root) %{py_sitedir}/PyKDE4/kparts.so
%attr(755,root,root) %{py_sitedir}/PyKDE4/ktexteditor.so
%attr(755,root,root) %{py_sitedir}/PyKDE4/kutils.so
%attr(755,root,root) %{py_sitedir}/PyKDE4/nepomuk.so
%attr(755,root,root) %{py_sitedir}/PyKDE4/phonon.so
%attr(755,root,root) %{py_sitedir}/PyKDE4/plasma.so
%attr(755,root,root) %{py_sitedir}/PyKDE4/polkitqt.so
%attr(755,root,root) %{py_sitedir}/PyKDE4/solid.so
%attr(755,root,root) %{py_sitedir}/PyKDE4/soprano.so
%{py_sitedir}/PyKDE4/__init__.py[co]
%{py_sitedir}/PyKDE4/pykdeconfig.py[co]

%files -n python-PyKDE4-devel
%defattr(644,root,root,755)
%dir %{_datadir}/sip/PyKDE4
%{_datadir}/sip/PyKDE4/akonadi
%{_datadir}/sip/PyKDE4/dnssd
%{_datadir}/sip/PyKDE4/kdecore
%{_datadir}/sip/PyKDE4/kdeui
%{_datadir}/sip/PyKDE4/khtml
%{_datadir}/sip/PyKDE4/kio
%{_datadir}/sip/PyKDE4/knewstuff
%{_datadir}/sip/PyKDE4/kparts
%{_datadir}/sip/PyKDE4/ktexteditor
%{_datadir}/sip/PyKDE4/kutils
%{_datadir}/sip/PyKDE4/nepomuk
%{_datadir}/sip/PyKDE4/phonon
%{_datadir}/sip/PyKDE4/plasma
%{_datadir}/sip/PyKDE4/polkitqt
%{_datadir}/sip/PyKDE4/solid
%{_datadir}/sip/PyKDE4/soprano
%{_datadir}/sip/PyKDE4/glossary.html

%files -n python-PyKDE4-devel-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pykdeuic4
%{py_sitedir}/PyQt4/uic/pykdeuic4.py*
%{py_sitedir}/PyQt4/uic/widget-plugins/kde4.py*

%files -n python-PyKDE4-examples
%defattr(644,root,root,755)
%{_examplesdir}/python-PyKDE4-%{version}
