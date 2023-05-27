%if price > 0:
    %euro = price // 100
    %cent = price % 100
    %cent = f'{cent:02d}'
                    <div class="price">{{euro}},{{cent}} €</div>
%else:
                    <div class="price sold">ausverkauft</div>
%end