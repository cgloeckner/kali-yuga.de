            <div class="item">
                <img class="preview" src="content/merch/cds/{{item}}.jpg" />
                <span>
                    <span class="title">{{data['type']}} „{{data['title']}}“ ({{data['year']}})</span>
%include('merch/price', price=data['price'])
                </span>
            </div>
