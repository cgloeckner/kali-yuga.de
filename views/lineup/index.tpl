%description = 'Die Geraer Death Metal Band KALI YUGA besteht aus Eik (Gitarre), Michael (Gitarre), Jan (Bass), Christian (Gesang) und Jean-Peer (Schlagzeug).'
%include('header', module_name='lineup')

<img class="title" alt="Kali Yuga Live Foto" src="{{get_static_url('/content/titles/lineup.jpg')}}">

<div class="lineup">

<h1 class="shifted">{{module_title}}</h1>

<h2 class="center">Aktuelle Besetzung</h2>

<div class="overview">
%for key in data:
    %include('lineup/member', key=key, data=data[key])
%end
</div>

<h2 class="center">Biografie</h2>

<h3>Gründung</h3>
<p>Ende 2006 begann der damalige Atanatos-Schlagzeuger Eik mit seinen Kumpels <i>Enrico</i> (E-Gitarre) und <i>David</i>
(Gesang) an eigenen Liedern zu arbeiten, um neue musikalische Wege zu gehen. Als dann mit <i>Florian</i> ein
Schlagzeuger gefunden  wurde und nach dem Aus von Atanatos mit <i>Kocher</i> noch ein Bassist mit zur Besetzung kam,
gründete sich nun eine  neue eigenständige Band namens Kali Yuga. Seit 2008 hielt Kali Yuga nun mit eigenen Songs
Auftritte in diversen Clubs und bei verschiedenen Festivals ab.

<h3>Besetzungskarussell</h3>
<p>2009 ergaben sich dann noch Besetzungswechsel: Für <i>David</i> kam <i>Grützer</i> (auch Gitarrist bei Artless) ans
Mikro und <i>Enricos</i> Job an der Gitarre übernahm <i>Michbert</i> von Radiation Dust. Mittels einer Promo-CD
<b>Dead Shall Reign</b>, aufgenommen im Rape of Harmonies Studio von Patrick W. Engel und Alexander Dietz im Jahr 2009,
konnte die Band verschiedene Labels auf sich aufmerksam machen und unterschrieb schließlich bei <b>G.U.C.</b> einen
Vertrag. Daraufhin folgten Auftritte zusammen mit Exodus, Graveworm, Dew-Scented, Watain und Tankard. Das erste Album
<b>Slaves to the Subliminal</b> erschien im Februar 2011. 2012 kam <i>Jean</i> in die Band und übernahm den
Schlagzeugerposten. Daraufhin schlossen sich diverse weitere Auftritte, darunter Konzerte auf dem Party.San oder dem
Hell Inside Festival an. Am 1. November 2012 erschien der nächste Tonträger <b>Wrath of Durga</b>.

<h3>Eine neue Stimme</h3>
<p>Nachdem <i>Grützer</i> 2017 seinen Rückzug vom Mikro bekannt gab, wurde nach langer Suche 2018 mit <i>Christian</i>
schließlich ein geeigneter Nachfolger gefunden. Die in der Zwischenzeit entstandenen Songs wurden vertextet. Alte und
neue Songs wurden Live präsentiert, bis die Corona-Pandemie den Jungs einen Strich durch die Rechnung machte. In dieser
Zeit began die Aufnahme des kommenden Albums <b>Lord of Lies</b> in Eigenregie. Eine Veröffentlichung ist für den
Jahreswechsel 2023/24 zu erwarten.
</p>

</div>

%include('footer')