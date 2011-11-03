# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/layouts
# catalog-date 2009-09-02 18:09:14 +0200
# catalog-license lppl1.3
# catalog-version 2.6d
Name:		texlive-layouts
Version:	2.6d
Release:	1
Summary:	Display various elements of a document's layout
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/layouts
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/layouts.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/layouts.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/layouts.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Display information about a document, including: text
positioning on a page; disposition of floats; layout of
paragraphs, lists, footnotes, table of contents, and sectional
headings; font boxes. Facilities are provided for a document
designer to experiment with the layout parameters.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
