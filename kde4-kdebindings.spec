%define		_state		stable
%define		orgname		kdebindings
Summary:	KDE bindings to non-C++ languages
Summary(pl.UTF-8):	Dowiązania KDE dla języków innych niż C++
Name:		kde4-kdebindings
Version:	4.1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	9c7ee50816ac6e0d5d2ea2f2968ac94d
BuildRequires:	QtGui-devel >= 4.4.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-kdepimlibs-devel >= %{version}
BuildRequires:	mono-csharp
BuildRequires:	python-PyQt4-devel >= 4.4.2
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	ruby-devel
BuildRequires:	python-sip
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
Group:		X11/Development/Libraries

%description kimono
C# Mono KDE4 bindings.

%description kimono -l pl.UTF-8
Dowiązania C# Mono do KDE4.

%package ruby-qt
Summary:	A SMOKE library for qt
Summary(pl.UTF-8):	Biblioteka SMOKE dla qt
Group:		X11/Development/Libraries

%description ruby-qt
A Qt bindings for Ruby using the SMOKE technology.

%description ruby-qt -l pl.UTF-8
Dowiązania Qt dla Ruby przy użyciu technologii SMOKE.

%package ruby-kde
Summary:	A SMOKE library for qt
Summary(pl.UTF-8):	Biblioteka SMOKE dla qt
Group:		X11/Development/Libraries

%description ruby-kde
A KDE bindings for Ruby using the SMOKE technology.

%description ruby-kde -l pl.UTF-8

%package ruby-devel
Summary:	Ruby header files
Summary(pl.UTF-8):	Pliki nagłówkowe dla ruby
Group:		X11/Development/Libraries

%description ruby-devel
Ruby header files.

%description ruby-devel -l pl.UTF-8
Pliki nagłówkowe dla ruby.

%package smoke-qt
Summary:	A SMOKE library for qt
Summary(pl.UTF-8):	Biblioteka SMOKE dla qt
Group:		X11/Development/Libraries

%description smoke-qt
SMOKE library (Scripting Meta Object Kompiler Engine) dla qt.

%description smoke-qt -l pl.UTF-8
Biblioteka SMOKE (Silnik kompilatora metaobiektów skryptowych) dla qt.

%package smoke-kde
Summary:	A SMOKE library for qt
Summary(pl.UTF-8):	Biblioteka SMOKE dla qt
Group:		X11/Development/Libraries

%description smoke-kde
SMOKE library (Scripting Meta Object Kompiler Engine) dla KDE4.

%description smoke-kde -l pl.UTF-8
Biblioteka SMOKE (Silnik kompilatora metaobiektów skryptowych) dla
KDE4.

%package smoke-devel
Summary:	smoke header files
Summary(pl.UTF-8):	Pliki nagłówkowe dla smoke
Group:		X11/Development/Libraries

%description smoke-devel
Smoke header files.

%description smoke-devel -l pl.UTF-8
Pliki nagłówkowe dla smoke.

%package -n python-PyKDE4
Summary:	Python bindings for KDE
Summary(pl.UTF-8):	Dowiązania do KDE dla Pyth
Group:		Libraries/Python

%description -n python-PyKDE4
PyKDE is a set of Python bindings for the KDE desktop environment. The
bindings are implemented as a set of Python modules: dcop, kdecore,
kdesu, kdefx (KDE 3.0 and later), kdeui, kio, kfile, kparts, khtml,
kjs, kspell and kdeprint (KDE 2.2.0 and later). The modules correspond
to libraries in the kdelibs package. PyKDE supports nearly all classes
and methods in these libraries.

%description -n python-PyKDE4 -l pl.UTF-8
PyKDE jest zbiorem dowiązań do KDE dla języka Python. Dowiązania są
zaimplementowane jako zbiór modułów Pythona: dcop, kdecore, kdesu,
kdefix (KDE 3.0 i późniejsze), kdeui, kio, kfile, kparts, khtml, kjs,
kspell i kdeprint (KDE 2.2.0 i późniejsze). Moduły odpowiadają
bibliotekom w pakiecie kdelibs. PyKDE wspiera prawie wszystkie klasy i
metody w wymienionych bibliotekach.

%package -n python-PyKDE4-examples
Summary:	PyKDE4 examples
Summary(pl.UTF-8):	Przykłady PyKDE4
Group:		Libraries/Python

%description -n python-PyKDE4-examples
PyKDE4 examples

%description -n python-PyKDE4-examples -l pl.UTF-8
Przykłady PyKDE4

%package -n qyoto
Summary:	C# Mono Qt4 bindings
Summary(pl.UTF-8):	Dowiązania C# Mono dla Qt4
Group:		X11/Development/Libraries

%description -n qyoto
C# Mono Qt4 bindings.

%description -n qyoto -l pl.UTF-8
Dowiązania C# Mono dla Qt4.

%package -n qyoto-devel
Summary:	qyoto header files
Summary(pl.UTF-8):	pliki nagłówkowe dla qyoto
Group:		X11/Development/Libraries

%description -n qyoto-devel
qyoto header files.

%description -n qyoto-devel -l pl.UTF-8
pliki nagłówkowe dla qyoto.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/pykde4
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

mv $RPM_BUILD_ROOT%{_datadir}/apps/pykde4/examples/* $RPM_BUILD_ROOT%{_examplesdir}/pykde4
%py_comp $RPM_BUILD_ROOT%{py_sitedir}/PyKDE4
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}/PyKDE4
%py_postclean

%find_lang pykde4 --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files kimono
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kimonopluginfactory.so
%attr(755,root,root) %{_libdir}/libkhtml-sharp.so
%attr(755,root,root) %{_libdir}/libnepomuk-sharp.so
%attr(755,root,root) %{_libdir}/libsoprano-sharp.so
%attr(755,root,root) %{_libdir}/libkimono.so
%dir %{_libdir}/mono
%{_libdir}/mono/2.0/kde-dotnet.dll
%{_libdir}/mono/2.0/khtml.dll
%{_libdir}/mono/2.0/soprano.dll
%{_libdir}/mono/2.0/nepomuk.dll
%{_libdir}/mono/gac/kde-dotnet
%{_libdir}/mono/gac/khtml
%{_libdir}/mono/gac/nepomuk
%{_libdir}/mono/gac/soprano

%files -n qyoto
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqyoto.so
%attr(755,root,root) %{_libdir}/libqyotoshared.so
%attr(755,root,root) %{_libdir}/libqtscript-sharp.so
%attr(755,root,root) %{_libdir}/libqtuitools-sharp.so
%attr(755,root,root) %{_libdir}/libqtwebkit-sharp.so
%dir %{_libdir}/mono/gac
%{_libdir}/mono/2.0/qt-dotnet.dll
%{_libdir}/mono/2.0/qtscript.dll
%{_libdir}/mono/2.0/qtuitools.dll
%{_libdir}/mono/2.0/qtwebkit.dll
%{_libdir}/mono/gac/qt-dotnet
%{_libdir}/mono/gac/qtscript
%{_libdir}/mono/gac/qtuitools
%{_libdir}/mono/gac/qtwebkit

%files -n qyoto-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/csrcc
%attr(755,root,root) %{_bindir}/uics
%{_includedir}/qyoto

%files smoke-qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsmokeqt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokeqt.so.?
%attr(755,root,root) %{_libdir}/libsmokeqtwebkit.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokeqtwebkit.so.?
%attr(755,root,root) %{_libdir}/libsmokeqtscript.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokeqtscript.so.?
%attr(755,root,root) %{_libdir}/libsmokeqtuitools.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokeqtuitools.so.?

%files smoke-kde
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsmokekde.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokekde.so.?
%attr(755,root,root) %{_libdir}/libsmokekhtml.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokekhtml.so.?
%attr(755,root,root) %{_libdir}/libsmokektexteditor.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokektexteditor.so.?
%attr(755,root,root) %{_libdir}/libsmokenepomuk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokenepomuk.so.?
%attr(755,root,root) %{_libdir}/libsmokephonon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokephonon.so.?
%attr(755,root,root) %{_libdir}/libsmokesolid.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokesolid.so.?
%attr(755,root,root) %{_libdir}/libsmokesoprano.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokesoprano.so.?
%attr(755,root,root) %{_libdir}/libsmokeqsci.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokeqsci.so.?

%files smoke-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsmokeqt.so
%attr(755,root,root) %{_libdir}/libsmokeqtwebkit.so
%attr(755,root,root) %{_libdir}/libsmokeqtscript.so
%attr(755,root,root) %{_libdir}/libsmokeqtuitools.so
%attr(755,root,root) %{_libdir}/libsmokekde.so
%attr(755,root,root) %{_libdir}/libsmokekhtml.so
%attr(755,root,root) %{_libdir}/libsmokektexteditor.so
%attr(755,root,root) %{_libdir}/libsmokenepomuk.so
%attr(755,root,root) %{_libdir}/libsmokephonon.so
%attr(755,root,root) %{_libdir}/libsmokesolid.so
%attr(755,root,root) %{_libdir}/libsmokesoprano.so
%attr(755,root,root) %{_libdir}/libsmokeqsci.so
%{_includedir}/smoke/*.h
%{_includedir}/smoke.h

%files ruby-qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rbqtapi
%attr(755,root,root) %{_bindir}/rbuic4
%attr(755,root,root) %{_bindir}/rbrcc
%attr(755,root,root) %{_libdir}/libqtruby4shared.so
%attr(755,root,root) %{ruby_sitearchdir}/qtruby4.so
%{ruby_sitelibdir}/Qt.rb
%{ruby_sitelibdir}/Qt3.rb
%{ruby_sitelibdir}/Qt4.rb
%{ruby_sitelibdir}/Qt/qtruby4.rb
%{ruby_sitelibdir}/Qt/active_item_model.rb
%{ruby_sitelibdir}/Qt/active_table_model.rb
%attr(755,root,root) %{ruby_sitearchdir}/qtwebkit.so
%{ruby_sitelibdir}/qtwebkit/qtwebkit.rb
%attr(755,root,root) %{ruby_sitearchdir}/qtuitools.so
%{ruby_sitelibdir}/qtuitools/qtuitools.rb
%attr(755,root,root) %{ruby_sitearchdir}/qtscript.so
%{ruby_sitelibdir}/qtscript/qtscript.rb

%files ruby-kde
%defattr(644,root,root,755)
%attr(755,root,root) %{ruby_sitearchdir}/phonon.so
%{ruby_sitelibdir}/phonon/phonon.rb
%attr(755,root,root) %{ruby_sitearchdir}/soprano.so
%{ruby_sitelibdir}/soprano/soprano.rb
%{_desktopdir}/kde4/dbpedia_references.desktop
%{_datadir}/apps/dbpedia_references/dbpedia_references.rb
%attr(755,root,root) %{ruby_sitearchdir}/korundum4.so
%attr(755,root,root) %{_libdir}/kde4/krubypluginfactory.so
%attr(755,root,root) %{_bindir}/krubyapplication
%{ruby_sitelibdir}/KDE/korundum4.rb
%attr(755,root,root) %{_bindir}/rbkconfig_compiler4
%attr(755,root,root) %{ruby_sitearchdir}/khtml.so
%{ruby_sitelibdir}/khtml/khtml.rb
%attr(755,root,root) %{ruby_sitearchdir}/ktexteditor.so
%{ruby_sitelibdir}/ktexteditor/ktexteditor.rb
%attr(755,root,root) %{ruby_sitearchdir}/nepomuk.so
%{ruby_sitelibdir}/nepomuk/nepomuk.rb
%attr(755,root,root) %{ruby_sitearchdir}/solid.so
%{ruby_sitelibdir}/solid/solid.rb
%attr(755,root,root) %{_libdir}/kde4/krossruby.so
%attr(755,root,root) %{_libdir}/kde4/krosspython.so

%files ruby-devel
%defattr(644,root,root,755)
%{_includedir}/qtruby/*.h

%files -n python-PyKDE4 -f pykde4.lang
%defattr(644,root,root,755)
%dir %{py_sitedir}/PyKDE4
%{py_sitedir}/PyKDE4/kdecore.so
%{py_sitedir}/PyKDE4/solid.so
%{py_sitedir}/PyKDE4/kdeui.so
%{py_sitedir}/PyKDE4/kio.so
%{py_sitedir}/PyKDE4/kutils.so
%{py_sitedir}/PyKDE4/kparts.so
%{py_sitedir}/PyKDE4/ktexteditor.so
%{py_sitedir}/PyKDE4/khtml.so
%{py_sitedir}/PyKDE4/knewstuff.so
%{py_sitedir}/PyKDE4/dnssd.so
%{py_sitedir}/PyKDE4/phonon.so
%{py_sitedir}/PyKDE4/soprano.so
%{py_sitedir}/PyKDE4/nepomuk.so
%{py_sitedir}/PyKDE4/akonadi.so
%{py_sitedir}/PyKDE4/__init__.py[co]
%{py_sitedir}/PyKDE4/pykdeconfig.py[co]
%{_datadir}/sip/PyKDE4/glossary.html

%dir %{_datadir}/apps/pykde4
%{_datadir}/apps/pykde4/kde4.py
%{_datadir}/apps/pykde4/kde4.pyc
%{_datadir}/apps/pykde4/pykdeuic4.py
%{_datadir}/apps/pykde4/pykdeuic4.pyc

%dir %{_datadir}/sip/PyKDE4
%{_datadir}/sip/PyKDE4/nepomuk
%{_datadir}/sip/PyKDE4/knewstuff
%{_datadir}/sip/PyKDE4/dnssd
%{_datadir}/sip/PyKDE4/solid
%{_datadir}/sip/PyKDE4/akonadi
%{_datadir}/sip/PyKDE4/kio
%{_datadir}/sip/PyKDE4/ktexteditor
%{_datadir}/sip/PyKDE4/khtml
%{_datadir}/sip/PyKDE4/soprano
%{_datadir}/sip/PyKDE4/kdecore
%{_datadir}/sip/PyKDE4/phonon
%{_datadir}/sip/PyKDE4/kdeui
%{_datadir}/sip/PyKDE4/kutils
%{_datadir}/sip/PyKDE4/kparts

%files -n python-PyKDE4-examples
%defattr(644,root,root,755)
%{_examplesdir}/pykde4
