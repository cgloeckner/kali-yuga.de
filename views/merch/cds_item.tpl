            <div class="item">
                <img class="preview" src="/content/cds/{{item['thumbnail']}}.jpg" />
                <span class="title">{{item['title']}}
%if 'spotify' in item:
                        <a class="listen" href="{{item['spotify']}}" target="_blank">
                            <img class="icon" src="https://open.spotifycdn.com/cdn/images/favicon.0f31d2ea.ico" />
                        </a>
%end
                </span>
                <span class="details">{{item['year']}} | {{item['type']}}</span>
%include('merch/price', price=item['price'])
            </div>
