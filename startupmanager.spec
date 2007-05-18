#
Summary:	StartUp Manager - a gui tool for changing settings in the bootloader and splash screen.
Summary(pl.UTF-8):	-
Name:		startupmanager
Version:	1.0.4
Release:	0.1
License:	GPL v.2
Group:		Applications
Source0:	http://web.telia.com/~u88005282/sum/archive/source/%{name}_%{version}-1.tar.gz
# Source0-md5:	7447b92ff541400a7959b0d2600cd3a6
Patch0:		%{name}-encoding.patch
URL:		http://web.telia.com/~u88005282/sum/
Requires:	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
StartUp Manager, or SUM, is a gui tool for changing settings
in the bootloader and splash screen.

%description -l pl.UTF-8

%prep
%setup -q
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT

export USER=root 
%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--prefix=%{_prefix}
		
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README 
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%dir %{py_sitescriptdir}/Startupmanager
%{py_sitescriptdir}/Startupmanager/*.py?
%{py_sitescriptdir}/Startupmanager/*.py
%{py_sitescriptdir}/Startupmanager/images/*.svg
%{py_sitescriptdir}/Startupmanager/*.glade
