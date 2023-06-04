%description = 'Mit einem Live-Set aus neuem aber auch bekannten Songmaterial steht die Geraer Death Metal Band KALI YUGA zur Verfügung. Anfragen an ' + booking_email
%include('header', module_name='gigs')

<img class="title" alt="Kali Yuga Live Foto" src="{{get_static_url('/content/titles/gigs.jpg')}}">

<div class="gigs">

<h1 class="shifted">{{module_title}}</h1>

<p class="center card">Unser Standort: 07549 Gera
    <br>
    <br>
    <b>Konzertanfragen an:</b><br>
    <a href="mailto:{{booking_email}}">{{booking_email}}</a>
</p>

%years_desc = sorted(data.keys(), key=lambda v: -v)
%for index, year in enumerate(years_desc):
    <div class="list toggle">
        <span onClick="toggleCollapse('gigs_{{year}}');">
            <h2><span id="gigs_{{year}}_button">&#9662;</span> {{year}}</h2>
        </span>
        <div id="gigs_{{year}}_container">
        %include('gigs/list', data=data[year])
        </div>
    </div>
%end

</div>

%include('footer')
