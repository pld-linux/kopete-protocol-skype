# NOTE:
# - to get source
# svn co svn://anonsvn.kde.org/home/kde/trunk/extragear/addons/kopete_skype
# cd kopete_skype
# svn co svn://anonsvn.kde.org/home/kde/branches/KDE/3.5/kde-common/admin
Summary:	Kopete plugin with Skype protocol support
Summary(pl):	Wtyczka Kopete obs³uguj±ca protokó³ Skype
Name:		kopete-protocol-skype
Version:	svn
Release:	0.1
License:	GPL
Group:		X11/Applications/Networking
Source0:	kopete_skype-20070110.622055.tar.bz2
# Source0-md5:	f2450e73eec57c0fb5de6fee043d8054
Patch0:		kde-common-PLD.patch
Patch1:		kde-ac260-lt.patch
Patch2:		kopete_skype-ac.patch
Patch3:		kopete_skype-srcdir.patch
Patch4:		kopete_skype-amd64.patch
URL:		http://websvn.kde.org/trunk/extragear/addons/kopete_skype/
BuildRequires:	automake
# https://developer.skype.com/Docs/ApiDoc/Using_the_Skype_API_on_Linux
BuildRequires:	dbus-devel < 0.24
BuildRequires:	kdelibs-devel
BuildRequires:	kdenetwork-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This adds Skype protocol support to Kopete.

%description -l pl
Ta wtyczka dodaje do Kopete obs³ugê protoko³u Skype.

%prep
%setup -q -n kopete_skype
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

touch INSTALL NEWS ChangeLog

%build
cp /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_libdir}/kde3/kopete_skype.la
%attr(755,root,root) %{_libdir}/kde3/kopete_skype.so
%{_datadir}/apps/kopete/icons/*/*/apps/skype_protocol.png
%{_datadir}/apps/kopete/icons/*/*/actions/call.png
%{_datadir}/apps/kopete/icons/*/*/actions/contact_ffc_overlay.png
%{_datadir}/apps/kopete/icons/*/*/actions/contact_unknown_overlay.png
%{_datadir}/apps/kopete/icons/*/*/actions/skype_connect.png
%dir %{_datadir}/apps/kopete_skype
%{_datadir}/apps/kopete_skype/call_end
%{_datadir}/apps/kopete_skype/call_start
%{_datadir}/apps/kopete_skype/skypechatui.rc
%{_datadir}/apps/kopete_skype/skypeui.rc
%{_iconsdir}/crystalsvg/*/actions/call.png
%{_iconsdir}/hicolor/*/actions/call.png
%{_datadir}/services/kopete_skype.desktop
