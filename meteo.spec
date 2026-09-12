%global appname com.gitlab.bitseater.%{name}
%global metainfodir %{_datadir}/metainfo

Name:           meteo
Version:        1.0.0
Release:        1%{?dist}
Summary:        Forecast application using OpenWeatherMap API
License:        GPLv3+
URL:            https://gitlab.com/bitseater/meteo
Source0:        %{name}-%{version}.tar.gz

%define DEPENS_RPM desktop-file-utils, rpmdevtools, git, gcc, wget, meson, ninja, vala, vala-devel, gettext, libgee-devel, gtk4-devel, libadwaita-devel, libsoup-devel, json-glib-devel, pkgconfig(webkitgtk-6.0), AppStream, fdupes

BuildRequires:  %{DEPENS_RPM}

%description
Know the forecast of the next hours & days.

Developed with Vala & Gtk, using OpenWeatherMap API.

Features:

- Current weather, with information about temperature, pressure, wind speed and
  direction, sunrise & sunset, moon phase.
- Forecast for next hours.
- Forecast for next days.
- Choose your units (metric, imperial or british).
- Choose your city.
- Awesome maps with weather info.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{appname}
%fdupes %{_datadir}/locale

%check
appstreamcli validate --no-net --explain %{buildroot}%{metainfodir}/%{appname}.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{appname}.desktop

%files
%license COPYING
%doc README.md AUTHORS CREDITS.md CHANGELOG
%{_bindir}/%{appname}
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/locale/*/LC_MESSAGES/%{appname}.mo
%{metainfodir}/*.metainfo.xml
%{_mandir}/man1/*.1*

%changelog
* Sat Sep 5 2026 Carlos Suárez (bitseater)
- Gtk4 & Libadwaita dependencies.
- Add Moon phases.
- Add system tray icon.
- New maps.
