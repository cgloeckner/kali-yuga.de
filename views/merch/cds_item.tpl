            <div class="item">
                <div class="title">{{data['title']}}</div>
                <img class="artwork" src="/content/cds/{{item}}.jpg" />
                <div class="listen">
%include('merch/cds_listen', data=data)
                </div>
                <div class="details">{{data['year']}}, {{data['type']}}</div>
%include('merch/price', price=data['price'])
            </div>
