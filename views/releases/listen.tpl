%if 'listen' in item:
    %for key in item['listen']:
        %if key == 'spotify':
                        <a class="listen" href="https://open.spotify.com/intl-de/album/{{item['listen']['spotify']}}" target="_blank">
                            <img class="icon" src="https://open.spotifycdn.com/cdn/images/favicon.0f31d2ea.ico">
                        </a>
        %end
    %end
%end