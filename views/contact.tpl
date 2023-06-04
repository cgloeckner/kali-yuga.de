%include('header', module_css='contact')

<div class="contact">

<br>
<br>
<br>
<br>

<h1>Kontakt</h1>

<div class="emails">

    <h2>Management &amp; Booking</h2>
    <p>
        <b>Eik Halle, Michael Albert</b><br>
        <a href="mailto:{{all_emails['booking']}}">{{all_emails['booking']}}</a>
    </p>

    <h2>Merchandise</h2>
    <p>
        <b>Jean-Peer Krutz</b><br>
        <a href="mailto:{{all_emails['merch']}}">{{all_emails['merch']}}</a>
    </p>

    <h2>Allgemeiner Kontakt</h2>
    <p>
        <b>Jan Koch</b><br>
        <a href="mailto:{{all_emails['contact']}}">{{all_emails['contact']}}</a>
    </p>

    <h2>Homepage</h2>
    <p>
        <b>Christian Glöckner</b><br>
        <a href="mailto:{{all_emails['webmaster']}}">{{all_emails['webmaster']}}</a>
    </p>

</div>

</div>

%include('footer')
