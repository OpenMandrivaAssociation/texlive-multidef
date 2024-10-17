Name:		texlive-multidef
Version:	40637
Release:	2
Summary:	Quickly define several similar macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/multidef
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multidef.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multidef.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multidef.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Multidef provides a simple way of defining several macros
having similar definitions.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/multidef
%{_texmfdistdir}/tex/latex/multidef
%doc %{_texmfdistdir}/doc/latex/multidef

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
