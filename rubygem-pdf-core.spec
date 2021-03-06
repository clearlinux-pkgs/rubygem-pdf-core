#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-pdf-core
Version  : 0.6.1
Release  : 8
URL      : https://rubygems.org/downloads/pdf-core-0.6.1.gem
Source0  : https://rubygems.org/downloads/pdf-core-0.6.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 Ruby
BuildRequires : ruby
BuildRequires : rubygem-pdf-inspector
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-simplecov

%description
No detailed description available

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n pdf-core-0.6.1
gem spec %{SOURCE0} -l --ruby > rubygem-pdf-core.gemspec

%build
gem build rubygem-pdf-core.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
pdf-core-0.6.1.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/pdf-core-0.6.1.gem
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/COPYING
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/GPLv2
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/GPLv3
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/lib/pdf/core.rb
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/lib/pdf/core/annotations.rb
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/lib/pdf/core/byte_string.rb
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/lib/pdf/core/destinations.rb
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/lib/pdf/core/document_state.rb
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/lib/pdf/core/filter_list.rb
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/lib/pdf/core/filters.rb
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/lib/pdf/core/graphics_state.rb
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/lib/pdf/core/literal_string.rb
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/lib/pdf/core/name_tree.rb
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/lib/pdf/core/object_store.rb
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/lib/pdf/core/outline_item.rb
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/lib/pdf/core/outline_root.rb
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/lib/pdf/core/page.rb
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/lib/pdf/core/page_geometry.rb
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/lib/pdf/core/pdf_object.rb
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/lib/pdf/core/reference.rb
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/lib/pdf/core/renderer.rb
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/lib/pdf/core/stream.rb
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/lib/pdf/core/text.rb
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/pdf-core.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/spec/decimal_rounding_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/spec/document_state_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/spec/filters_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/spec/name_tree_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/spec/object_store_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/spec/pdf_object_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/spec/reference_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/pdf-core-0.6.1/spec/stream_spec.rb
/usr/lib64/ruby/gems/2.3.0/specifications/pdf-core-0.6.1.gemspec
