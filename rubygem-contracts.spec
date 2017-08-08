# Generated from contracts-0.14.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name contracts

Name: rubygem-%{gem_name}
Version: 0.14.0
Release: 2%{?dist}
Summary: Contracts for Ruby
Group: Development/Languages
License: BSD-2-Clause
URL: http://github.com/egonSchiele/contracts.ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
# the following BuildRequires are development dependencies
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
This library provides contracts for Ruby. Contracts let you clearly express
how your code behaves, and free you from writing tons of boilerplate,
defensive code.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/




# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%{gem_instdir}/.rspec
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE
%{gem_instdir}/TODO.markdown
%{gem_instdir}/TUTORIAL.md
%{gem_instdir}/benchmarks
%{gem_instdir}/cucumber.yml
%{gem_instdir}/features
%{gem_libdir}
%{gem_instdir}/script
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.markdown
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/contracts.gemspec
%{gem_instdir}/spec

%changelog
* Fri Sep 23 2016 Rich Megginson <rmeggins@redhat.com> - 0.14.0-2
- bump rel to rebuild for rhlog-buildrequires

* Thu Sep 22 2016 Rich Megginson <rmeggins@redhat.com> - 0.14.0-1
- Initial package
