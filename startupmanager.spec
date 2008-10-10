# TODO: py_postclean
Summary:	StartUp Manager - GUI tool for changing settings in the bootloader and splash screen
Summary(pl.UTF-8):	StartUp Manager - interfejs graficzny dla bootloadera i ekranu startowego
Name:		startupmanager
Version:	1.9.11
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://downloads.sourceforge.net/startup-manager/%{name}-%{version}.tar.gz
# Source0-md5:	b20c8e965b64b5047c33c9a811bca9c3
URL:		http://web.telia.com/~u88005282/sum/
BuildRequires:	gnome-doc-utils
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
StartUp Manager, or SUM, is a gui tool for changing settings
in the bootloader and splash screen.

%description -l pl.UTF-8
StartUp Manager, lub w skrócie SUM, jest interfejsem graficznym dla
bootloadera i ekranu startowego (splashscreena).

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

export USER=root 
%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--prefix=%{_prefix}
		
%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README 
%attr(755,root,root) %{_sbindir}/*
%{_desktopdir}/*.desktop
%{_desktopdir}/kde/*.desktop
%dir %{py_sitescriptdir}/bootconfig
%{py_sitescriptdir}/bootconfig/*.py?
%{py_sitescriptdir}/bootconfig/*.py
%{py_sitescriptdir}/*.egg-info
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.py
%{_datadir}/%{name}/*.glade
%{_datadir}/%{name}/*.svg
