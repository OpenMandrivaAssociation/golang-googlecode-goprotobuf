%global goipath         github.com/golang/protobuf
Version:                1.2.0

%gometa

Name:           golang-googlecode-goprotobuf
Release:        1%{?dist}
Summary:        Go support for Google protocol buffers
License:        BSD
URL:            %gourl
Source0:        %gosource

BuildRequires:  protobuf-compiler
Requires:       protobuf
Provides:       protoc-gen-go = %{version}-%{release}

%description
This package provides support for protocol buffers in the form of a protocol
compiler plugin which generates Go source files that, once compiled, can access
and manage protocol buffers.

Install %{name}-devel for the associated support library.

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
This package provides  a library that implements run-time support for
encoding (marshaling), decoding (unmarshaling), and accessing protocol
buffers in the Go language.

Install %{name} for the related protocol compiler plugin.

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgesetup

%build
%gobuildroot

%gobuild -o _bin/protoc-gen-go %{goipath}/protoc-gen-go

%install
install -d %{buildroot}%{_bindir}
install -m 755 _bin/protoc-gen-go %{buildroot}/%{_bindir}/protoc-gen-go

# source codes for building projects
files=$(find . -name "testdata" -type d)
%goinstall $files

%check
export PATH=$PATH:$(pwd)/_bin
%gochecks -d proto/testdata -d proto

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%doc AUTHORS CONTRIBUTORS LICENSE README.md
%{_bindir}/protoc-gen-go

%files devel -f devel.file-list
%license LICENSE
%doc *.md AUTHORS CONTRIBUTORS

%changelog
* Thu Oct 25 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.0-1
- Update to release 1.2.0

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 1.0.0-3
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 31 2018 Paul Gier <pgier@redhat.com> - 1.0.0-1
- Update to release 1.0.0

* Mon May 07 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.37.git5afd06f
- Rename binary to protoc-gen-go
- Fix bug #1567650

* Sun Mar 18 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.36.git5afd06f
- Bump to 5afd06f9d81a86d6e3bb7dc702d6bd148ea3ff23

* Fri Mar 09 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.35.git5a0f697
- Bump to 5a0f697c9ed9d68fef0116532c6e05cfeae00e55

* Sun Mar 04 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.34.git24f28ae
- Update to spec 3.0

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.33.20161116git24f28ae
- Exclude _conformance directory

* Tue Feb 20 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.32.git24f28ae
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.31.git24f28ae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 18 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.30.git24f28ae
- Bump to upstream 24f28ae800abfde9310e779f94be606b1a98a3fc
  resolves: #1474510

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.29.git4bd1920
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.28.git4bd1920
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 16 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.27.git4bd1920
- Bump to upstream 4bd1920723d7b7c925de087aa32e2187708897f7
  related: #1246113

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.26.git8616e8e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 15 2016 Jan Chaloupka <jchaloup@redhat.com> - 0-0.25.git8616e8e
- Polish the spec file
  related: #1246113

* Wed Jul 27 2016 jchaloup <jchaloup@redhat.com> - 0-0.24.git8616e8e
- Polish the spec file
  related: #1246113

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.23.git8616e8e
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Jul 11 2016 jchaloup <jchaloup@redhat.com> - 0-0.22.git8616e8e
- Bump to upstream 8616e8ee5e20a1704615e6c8d7afcdac06087a67
  related: #1246113

* Tue Mar 22 2016 jchaloup <jchaloup@redhat.com> - 0-0.21.git6aaa8d4
- Bump to upstream 6aaa8d47701fa6cf07e914ec01fde3d4a1fe79c3
  related: #1246113

* Sun Mar 06 2016 jchaloup <jchaloup@redhat.com> - 0-0.20.git3d2510a
- Bump to upstream 3d2510a4dd961caffa2ae781669c628d82db700a
  related: #1246113

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.19.git0f7a9ca
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.git0f7a9ca
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 24 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0-0.17.git446d52d
- Change deps on compiler(go-compiler)
- Update Arches
- Use %%license

* Thu Jul 23 2015 jchaloup <jchaloup@redhat.com> - 0-0.16.git0f7a9ca
- Bump to upstream 0f7a9caded1fb3c9cc5a9b4bcf2ff633cc8ae644
- Update spec file to spec-2.0
  resolves: #1246113

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.15.gitefd7476
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 09 2015 jchaloup <jchaloup@redhat.com> - 0-0.14.gitefd7476
- Bump to upstream efd7476481382c195beb33acd8ec2f1527167fb4
  related: #1018057

* Thu Mar 05 2015 jchaloup <jchaloup@redhat.com> - 0-0.13.gitc22ae3c
- Bump to upstream c22ae3cf020a21ebb7ae566dccbe90fc8ea4f9ea
  related: #1018057

* Sun Feb 08 2015 jchaloup <jchaloup@redhat.com> - 0-0.12.git7f07925
- Extend Provides for proto/testdata
  related: #1018057

* Fri Jan 30 2015 jchaloup <jchaloup@redhat.com> - 0-0.11.git7f07925
- Provide back compatibility provides
  resolves: #1187495 #1187491 #1187494

* Mon Jan 26 2015 jchaloup <jchaloup@redhat.com> - 0-0.10.git7f07925
- Bump to 7f07925444bb51fa4cf9dfe6f7661876f8852275
  related: #1018057

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.hg61664b8425f3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.hg61664b8425f3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 17 2013 Lokesh Mandvekar <lsm5@redhat.com> - 0-0.7.hg61664b8425f3
- removed double quotes from provides

* Wed Oct 16 2013 Peter Lemenkov <lemenkov@gmail.com> - 0-0.6.hg61664b8425f3
- Added missing buildrequires

* Mon Oct 14 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.5.hg61664b8425f3
- description update

* Mon Oct 14 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.4.hg61664b8425f3
- defattr removed
- docs included in base and devel packages

* Sat Oct 12 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.3.hg61664b8425f3
- testdata directories excluded

* Sat Oct 12 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.2.hg61664b8425f3
- compiler plugin in archful base package
- libraries in noarch (except rhel6) devel subpackage

* Fri Oct 11 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.1.hg61664b8425f3
- Initial fedora package
