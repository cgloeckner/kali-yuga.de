            <div class="item">
                <img class="preview" src="/content/cds/{{item}}.jpg" />
                <span class="title">{{data['title']}}
%include('merch/cds_listen', data=data)
                </span>
                <span class="details">{{data['year']}} | {{data['type']}}</span>
%include('merch/price', price=data['price'])
            </div>
