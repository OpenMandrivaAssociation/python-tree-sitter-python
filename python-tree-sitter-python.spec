Name:		python-tree-sitter-python
Version:	0.25.0
Release:	1
Summary:	Tree-sitter python grammar (Python bindings)
License:	MIT
Group:		Development/Python
URL:		https://github.com/tree-sitter/tree-sitter-python
Source0:	https://files.pythonhosted.org/packages/b8/8b/c992ff0e768cb6768d5c96234579bf8842b3a633db641455d86dd30d5dac/tree_sitter_python-0.25.0.tar.gz
# PyPI sdist omits src/scanner.c; parser.c still references it
Source1:	tree-sitter-python-scanner.c
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	clang
Requires:	python%{pyver}dist(tree-sitter)

%description
Tree-sitter grammar for python, compiled from source. Used by
Aider's grep-ast repo-map.

%prep
%autosetup -n tree_sitter_python-0.25.0
cp %{SOURCE1} src/scanner.c

%build

%install
export CC=clang
python -m pip install \
	--no-deps --no-build-isolation --no-compile \
	--root %{buildroot} --prefix %{_prefix} \
	.

%files
%doc README.md
%license LICENSE
%{python_sitearch}/tree_sitter_python
%{python_sitearch}/tree_sitter_python-*.*-info
