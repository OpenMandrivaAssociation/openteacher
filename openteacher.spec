Name:		openteacher
Version:	2.2.1
Release:	%mkrel 2
Summary:	An application that helps you learn a foreign language
License:	GPLv3+
Group:		Education
URL:		http://openteacher.org/
Source0:	http://launchpad.net/openteacher/2.x/2.2/+download/%{name}-%{version}.tar.gz
Patch0:		openteacher-2.2.1-desktop.patch
Patch1:		openteacher-2.2.1-setup.patch
BuildRequires:	python-devel
Requires:	PyQt4
BuildArch:	noarch

%description
OpenTeacher has the following features:
- Smart and interval question asking
- Think answer, shuffle answer and repeat answer input modes
- Easy symbol, Greek and Cyrillic input
- Read and write Teach2000 and WRTS files, read ABBY Lingvo Tutor files
- Save and open your online WRTS lists
- Support for synonyms
- Printing your word lists
- Available in Arabic, Trad. Chinese, Croatian, Danish, Dutch, English,
  French, German, Hebrew, Hungarian, Japanese, Korean, Polish, Russian,
  Serbian, Slovenian, Spanish, Swedish and Turkish.

%prep
%setup -q -c
%patch0 -p1 -b .desktop
%patch1 -p1 -b .setup

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
%__python setup.py install \
	--root=%{buildroot} \
	--no-compile

%__install -d %{buildroot}%{_datadir}/applications
%__install -m 644 linux/%{name}.desktop %{buildroot}%{_datadir}/applications/

%__install -d %{buildroot}%{_iconsdir}/hicolor/48x48/apps
%__install -m 644 linux/%{name}.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/

%__install -d %{buildroot}%{_iconsdir}/hicolor/48x48/mimetypes
%__install -m 644 linux/application*.png %{buildroot}%{_iconsdir}/hicolor/48x48/mimetypes/

%__install -d %{buildroot}%{_datadir}/mime/packages
%__install -m 644 linux/%{name}.xml %{buildroot}%{_datadir}/mime/packages/

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING NEWS README
%{_bindir}/%{name}
%{python_sitelib}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/*/mimetypes/application*.png



%changelog
* Tue Nov 15 2011 Andrey Bondrov <abondrov@mandriva.org> 2.2.1-2mdv2011.0
+ Revision: 730716
- Change category in XDG menu (Education -> Education/Languages)

* Mon Nov 14 2011 Andrey Bondrov <abondrov@mandriva.org> 2.2.1-1
+ Revision: 730539
- imported package openteacher

