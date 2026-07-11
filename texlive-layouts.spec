%global tl_name layouts
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.6d
Release:	%{tl_revision}.1
Summary:	Display various elements of a documents layout
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/layouts
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/layouts.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/layouts.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/layouts.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Display information about a document, including: text positioning on a
page; disposition of floats; layout of paragraphs, lists, footnotes,
table of contents, and sectional headings; font boxes. Facilities are
provided for a document designer to experiment with the layout
parameters.

