%global tl_name multidef
%global tl_revision 40637

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.10
Release:	%{tl_revision}.1
Summary:	Quickly define several similar macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/multidef
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multidef.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multidef.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multidef.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Multidef provides a simple way of defining several macros having similar
definitions.

