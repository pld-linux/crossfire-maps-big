Summary:	Maps for Crossfire, the multiplayer roguelike game server
Summary(pl):	Mapy do Crossfire, serwera gry roguelike dla wielu graczy
Name:		crossfire-maps-big
Version:	1.6.0
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/crossfire/crossfire-%{version}.maps-big.tar.bz2
# Source0-md5:	e5aa783d65ba8c224a75f075d3820ab1
URL:		http://crossfire.real-time.com/
BuildArch:	noarch
Provides:	crossfire-maps
Obsoletes:	crossfire-maps
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crossfire is a multiplayer graphical arcade and adventure game made
for the X-Window environment. There are also Windows and Java clients
available. This package contains default maps describing game's world.

%description -l pl
To jest graficzna gra przygodowa dla ¶rodowiska X-Window. S± tak¿e
dostêpni klienci pod Windows i w Javie. Ten pakiet zawiera standardowe
mapy opisuj±ce ¶wiat gry.

%prep
%setup -qn maps-bigworld

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/crossfire/maps/scripts

mv * $RPM_BUILD_ROOT%{_datadir}/crossfire/maps
mv .* $RPM_BUILD_ROOT%{_datadir}/crossfire/maps
mv $RPM_BUILD_ROOT%{_datadir}/crossfire/maps/Info .
mv Info/*.pl $RPM_BUILD_ROOT%{_datadir}/crossfire/maps/scripts

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- crossfire-maps < 1.5.0
if [ "$1" != "0" ]; then
	su games -c "
		find /var/lib/crossfire/players/ -maxdepth 1 -mindepth 1 -printf '%%p/\n' \
		| xargs perl %{_datadir}/crossfire/maps/scripts/update_apart.pl ;
		perl %{_datadir}/crossfire/maps/scripts/update_apart.pl \
				/var/lib/crossfire/unique-items/"
fi

%triggerpostun -- crossfire-maps-small
if [ "$1" != "0" ]; then
	su games -c "
		find /var/lib/crossfire/players/ -maxdepth 1 -mindepth 1 -printf '%%p/\n' \
		| xargs perl %{_datadir}/crossfire/maps/scripts/update_apart.pl ;
		perl %{_datadir}/crossfire/maps/scripts/update_apart.pl \
				/var/lib/crossfire/unique-items/"
fi

%files
%defattr(644,root,root,755)
%doc Info/*
%{_datadir}/crossfire/maps
