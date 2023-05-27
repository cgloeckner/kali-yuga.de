%include('header')

<div class="gigs">

<h1>Live Shows</h1>

<p class="center"><a href="mailto:booking@kali-yuga.de">booking@kali-yuga.de</a></p>

%years_desc = sorted(data.keys(), key=lambda v: -v)
%for year in years_desc:
    <h2>{{year}}</h2>
    %include('gigs/list', data=data[year])
%end

</div>

%include('footer')
