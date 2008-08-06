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
BuildRequires:	python-PyQt4-devel >= 4.4.2
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bindings for the K Desktop Environment: provide interfaces to many
diferent programming languages to use KDE native resources and
widgets.

%description -l pl.UTF-8
Dowiązania KDE/qt dla języków innych niż C++ pozwalające używać
natywnych dla KDE zasobów i widgetów.

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

%package smoke-qt
Summary:	A SMOKE library for qt
Summary(pl.UTF-8):	Biblioteka SMOKE dla qt
Group:		X11/Development/Libraries

%description smoke-qt
SMOKE library (Scripting Meta Object Kompiler Engine) dla qt.

%description smoke-qt -l pl.UTF-8
Biblioteka SMOKE (Silnik kompilatora metaobiektów skryptowych) dla qt.

%package smoke-qt-devel
Summary:	smoke-qt header files
Summary(pl.UTF-8):	Pliki nagłówkowe dla smoke-qt
Group:		X11/Development/Libraries

%description smoke-qt-devel
smoke-qt header files.

%description smoke-qt-devel -l pl.UTF-8
Pliki nagłówkowe dla smoke-qt.

%package smoke-kde
Summary:	A SMOKE library for qt
Summary(pl.UTF-8):	Biblioteka SMOKE dla qt
Group:		X11/Development/Libraries

%description smoke-kde
SMOKE library (Scripting Meta Object Kompiler Engine) dla KDE.

%description smoke-kde -l pl.UTF-8
Biblioteka SMOKE (Silnik kompilatora metaobiektów skryptowych) dla
KDE.

%package smoke-kde-devel
Summary:	smoke-qt header files
Summary(pl.UTF-8):	Pliki nagłówkowe dla smoke-qt
Group:		X11/Development/Libraries

%description smoke-kde-devel
smoke-kde header files.

%description smoke-kde-devel -l pl.UTF-8
Pliki nagłówkowe dla smoke-kde.

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

%find_lang pykde4 --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files smoke-qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsmokeqt.so.2.0.0
%attr(755,root,root) %{_libdir}/libsmokeqtwebkit.so.2.0.0
%attr(755,root,root) %{_libdir}/libsmokeqtscript.so.2.0.0
%attr(755,root,root) %{_libdir}/libsmokeqtuitools.so.2.0.0

%files smoke-qt-devel
%defattr(644,root,root,755)
%{_includedir}/smoke/*.h
%{_includedir}/smoke.h

%files smoke-kde
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsmokekde.so.2.0.0
%attr(755,root,root) %{_libdir}/libsmokekhtml.so.2.0.0
%attr(755,root,root) %{_libdir}/libsmokektexteditor.so.2.0.0
%attr(755,root,root) %{_libdir}/libsmokenepomuk.so.2.0.0
%attr(755,root,root) %{_libdir}/libsmokephonon.so.2.0.0
%attr(755,root,root) %{_libdir}/libsmokesolid.so.2.0.0
%attr(755,root,root) %{_libdir}/libsmokesoprano.so.2.0.0
%{_libdir}/libsmokekde.so
%attr(755,root,root) %{_libdir}/libsmokekde.so.2
%{_libdir}/libsmokekhtml.so
%attr(755,root,root) %{_libdir}/libsmokekhtml.so.2
%{_libdir}/libsmokektexteditor.so
%attr(755,root,root) %{_libdir}/libsmokektexteditor.so.2
%{_libdir}/libsmokenepomuk.so
%attr(755,root,root) %{_libdir}/libsmokenepomuk.so.2
%{_libdir}/libsmokephonon.so
%attr(755,root,root) %{_libdir}/libsmokephonon.so.2
%{_libdir}/libsmokeqt.so
%attr(755,root,root) %{_libdir}/libsmokeqt.so.2
%{_libdir}/libsmokeqtscript.so
%attr(755,root,root) %{_libdir}/libsmokeqtscript.so.2
%{_libdir}/libsmokeqtuitools.so
%attr(755,root,root) %{_libdir}/libsmokeqtuitools.so.2
%{_libdir}/libsmokeqtwebkit.so
%attr(755,root,root) %{_libdir}/libsmokeqtwebkit.so.2
%{_libdir}/libsmokesolid.so
%attr(755,root,root) %{_libdir}/libsmokesolid.so.2
%{_libdir}/libsmokesoprano.so
%attr(755,root,root) %{_libdir}/libsmokesoprano.so.2

#%files smoke-kde-devel
#%defattr(644,root,root,755)

%files ruby-qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rbqtapi
%attr(755,root,root) %{_bindir}/rbuic4
%attr(755,root,root) %{_bindir}/rbrcc
%{_libdir}/libqtruby4shared.so
%{ruby_sitearchdir}/qtruby4.so
%{ruby_sitelibdir}/Qt.rb
%{ruby_sitelibdir}/Qt4.rb
%{ruby_sitelibdir}/Qt3.rb
%{ruby_sitelibdir}/Qt/qtruby4.rb
%{ruby_sitelibdir}/Qt/active_item_model.rb
%{ruby_sitelibdir}/Qt/active_table_model.rb
%{ruby_sitearchdir}/qtwebkit.so
%{ruby_sitelibdir}/qtwebkit/qtwebkit.rb
%{ruby_sitearchdir}/qtuitools.so
%{ruby_sitelibdir}/qtuitools/qtuitools.rb
%{ruby_sitearchdir}/qtscript.so
%{ruby_sitelibdir}/qtscript/qtscript.rb

%files ruby-kde
%defattr(644,root,root,755)
%{ruby_sitearchdir}/phonon.so
%{ruby_sitelibdir}/phonon/phonon.rb
%{ruby_sitearchdir}/soprano.so
%{ruby_sitelibdir}/soprano/soprano.rb
%{_desktopdir}/kde4/dbpedia_references.desktop
%{_datadir}/apps/dbpedia_references/dbpedia_references.rb
%{ruby_sitearchdir}/korundum4.so
%{_libdir}/kde4/krubypluginfactory.so
%attr(755,root,root) %{_bindir}/krubyapplication
%{ruby_sitelibdir}/KDE/korundum4.rb
%attr(755,root,root) %{_bindir}/rbkconfig_compiler4
%{ruby_sitearchdir}/khtml.so
%{ruby_sitelibdir}/khtml/khtml.rb
%{ruby_sitearchdir}/ktexteditor.so
%{ruby_sitelibdir}/ktexteditor/ktexteditor.rb
%{ruby_sitearchdir}/nepomuk.so
%{ruby_sitelibdir}/nepomuk/nepomuk.rb
%{ruby_sitearchdir}/solid.so
%{ruby_sitelibdir}/solid/solid.rb
%{_libdir}/kde4/krossruby.so
%{_libdir}/kde4/krosspython.so

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
%{py_sitedir}/PyKDE4/soprano.so/
%{py_sitedir}/PyKDE4/nepomuk.so
%{py_sitedir}/PyKDE4/akonadi.so
%{py_sitedir}/PyKDE4/__init__.py
%{py_sitedir}/PyKDE4/__init__.pyc
%{py_sitedir}/PyKDE4/pykdeconfig.py
%{py_sitedir}/PyKDE4/pykdeconfig.pyc
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
