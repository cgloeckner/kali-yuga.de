        <div class="release">
            <img class="preview" src="/content/cds/{{item['thumbnail']}}.jpg">
            <div class="column">
                <div class="title">{{item['title']}}</div>
                <div class="description">{{item['year']}} | {{item['type']}}
%include('releases/listen', item=item)
                </div>
                <div class="tracklist"><b>Tracklist:</b>
                    <ol>
%for track in item['tracks']:
                        <li>{{track}}</li>
%end
                    </ol>
                </div>
            </div>
        </div>