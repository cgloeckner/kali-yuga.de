%description = 'Mit einem Live-Set aus neuem aber auch bekannten Songmaterial steht die Geraer Death Metal Band KALI YUGA zur Verfügung. Anfragen an ' + booking_email
%include('header', module_name='gigs')

<img class="title" alt="Kali Yuga Live Foto" src="{{get_static_url('/content/titles/gigs.jpg')}}">

<div class="gigs">

<h1 class="shifted">{{module_title}}</h1>

<p class="center"><a href="mailto:{{booking_email}}">{{booking_email}}</a></p>

%years_desc = sorted(data.keys(), key=lambda v: -v)
%for year in years_desc:
    <div class="list">
        <h2>{{year}}</h2>
        %include('gigs/list', data=data[year])
    </div>
%end

</div>

%include('footer')
