# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/layouts
# catalog-date 2009-09-02 18:09:14 +0200
# catalog-license lppl1.3
# catalog-version 2.6d
Name:		texlive-layouts
Version:	2.6d
Release:	6
Summary:	Display various elements of a document's layout
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/layouts
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/layouts.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/layouts.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/layouts.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.6d-2
+ Revision: 753207
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.6d-1
+ Revision: 718834
- texlive-layouts
- texlive-layouts
- texlive-layouts
- texlive-layouts

