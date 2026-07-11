%global tl_name flashmovie
%global tl_revision 25768

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4
Release:	%{tl_revision}.1
Summary:	Directly embed flash movies into PDF files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/flashmovie
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/flashmovie.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/flashmovie.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows direct embedding of flash movies into PDF files. It
is designed for use with pdfLaTeX. The package takes advantage of the
embedded Adobe Flash player in Adobe Reader 9; the reader is invoked
with the 'rich media annotation' feature, described in "Adobe Supplement
to the ISO 32000 BaseVersion: 1.7 ExtensionLevel: 3". This method of
embedding movies is attractive since it removes all platform
dependencies; however, the user is required to use Acrobat 9.

