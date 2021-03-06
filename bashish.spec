# norootforbuild

%define _prefix	/usr

Name:		bashish
Version:	2.2.4
Release:	1.bashish.generic
Summary:	Theme Environment For Text Terminals
Source:		http://prdownloads.sourceforge.net/bashish/bashish-%{version}.tar.gz
URL:		http://bashish.sourceforge.net/
Group:		System/Shells
Packager:	Thomas Eriksson <arne@users.sourceforge.net>
License:	GPL
BuildRoot:	%{_tmppath}/build-%{name}-%{version}
Requires:	bash dialog
BuildRequires:  autoconf bash
BuildArch:	noarch

%description
Bashish is a theme enviroment for text terminals. It can
change colors, font, transparency, and background image 
on a per-application basis. Additionally Bashish supports
prompt changing on common shells such as bash, zsh, and 
tcsh.

%prep
%setup -q
autoreconf -fiv
%configure --with-shell=/bin/bash

%build
%__make

%install
make DESTDIR=%{buildroot} install

%clean
%__rm -rf "%{buildroot}"

%files
%defattr(-,root,root)
%doc %{_docdir}/%{name}/*
%{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/bashish-version
%dir %{_datadir}/%{name}/defaults
%{_datadir}/%{name}/defaults/*
%dir %{_datadir}/%{name}/overrides
%{_datadir}/%{name}/overrides/*
%{_datadir}/%{name}/lib
%{_datadir}/%{name}/main
%dir %{_datadir}/%{name}/themes
%dir %{_datadir}/%{name}/themes/app
%{_datadir}/%{name}/themes/app/*
%dir %{_datadir}/%{name}/themes/ascii-art
%{_datadir}/%{name}/themes/ascii-art/*
%dir %{_datadir}/%{name}/themes/computer
%{_datadir}/%{name}/themes/computer/*
%doc %{_mandir}/man1/bashish.1*

%changelog

* Sat Jul 15 2010 Thomas Eriksson <arne@users.sourceforge.net> 2.0.6-1
- removed fillx manpage

* Fri Jul 14 2010 Thomas Eriksson <arne@users.sourceforge.net> 2.0.5-1
- removed fillx manpage

* Thu Jun 15 2010 Thomas Eriksson <arne@users.sourceforge.net> 2.0.4-1
- fixed doc destination dir
- added fillx manpage

* Wed Jun 14 2010 Thomas Eriksson <arne@users.sourceforge.net> 2.0.4-1
- fixes, removed SuSE specific code

* Sun Mar 12 2010 Pascal Bleser <guru@unixtech.be> 2.0.3-1
- new package

# Local Variables:
# mode: rpm-spec
# tab-width: 8
# End:
