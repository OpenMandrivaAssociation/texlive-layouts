Name:		texlive-layouts
Version:	42428
Release:	2
Summary:	Display various elements of a document's layout
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/layouts
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/layouts.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/layouts.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/layouts.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Display information about a document, including: text
positioning on a page; disposition of floats; layout of
paragraphs, lists, footnotes, table of contents, and sectional
headings; font boxes. Facilities are provided for a document
designer to experiment with the layout parameters.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/layouts/layouts.sty
%doc %{_texmfdistdir}/doc/latex/layouts/README
%doc %{_texmfdistdir}/doc/latex/layouts/layman.pdf
%doc %{_texmfdistdir}/doc/latex/layouts/layouts.pdf
#- source
%doc %{_texmfdistdir}/source/latex/layouts/layman.tex
%doc %{_texmfdistdir}/source/latex/layouts/layouts.dtx
%doc %{_texmfdistdir}/source/latex/layouts/layouts.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
