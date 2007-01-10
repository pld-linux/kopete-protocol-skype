# NOTE:
# - to get source
# svn co svn://anonsvn.kde.org/home/kde/trunk/extragear/addons/kopete_skype
# cd kopete_skype
# svn co svn://anonsvn.kde.org/home/kde/branches/KDE/3.5/kde-common/admin
Summary:	Multi-protocol plugin-based instant messenger
Name:		kopete-protocol-skype
Version:	svn
Release:	0.1
License:	GPL
Group:		X11/Applications/Networking
Source0:	kopete_skype-20070110.622055.tar.bz2
# Source0-md5:	f2450e73eec57c0fb5de6fee043d8054
URL:		http://websvn.kde.org/trunk/extragear/addons/kopete_skype/
BuildRequires:	automake
#BuildRequires:	kopete-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This adds Skype protocol support to Kopete.

%prep
%setup -q -n kopete_skype

%build
cp /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs
%configure

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
