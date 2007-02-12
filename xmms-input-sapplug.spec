Summary:	SAP music input plugin for XMMS
Summary(pl.UTF-8):	Wtyczka wejściowa dla XMMS-a odtwarzająca muzykę w formacie SAP
Name:		xmms-input-sapplug
Version:	0.31
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://asma.atari.org/bin/sapplug-xmms-%{version}.tar.gz
# Source0-md5:	f9a098f9f4a24ffc52c1f976e6857651
URL:		http://asma.atari.org/
BuildRequires:	libsap-devel
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel >= 1.2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin allows XMMS to play SAP (Atari XL/XE) music files.

%description -l pl.UTF-8
Ta wtyczka pozwala XMMS-owi odtwarzać pliki muzyczne w formacie SAP
(Atari XL/XE).

%prep
%setup -q -n sapplug-xmms-%{version}

rm -f saplib/*
ln -sf /usr/include/libsap.h saplib/sapLib.h

%build
%{__make} plugin \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC -Wall -ffast-math `xmms-config --cflags`" \
	SAPLIB="-lsap"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{xmms_input_plugindir}

install libsap.so $RPM_BUILD_ROOT%{xmms_input_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{CHANGES,CREDITS,README,TODO}
%attr(755,root,root) %{xmms_input_plugindir}/libsap.so
