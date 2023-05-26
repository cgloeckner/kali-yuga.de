%if price > 0:
    %euro = price // 100
    %cent = price % 100
    %cent = f'{cent:02d}'
                    <span class="price">{{euro}},{{cent}} €</span>
%else:
                    <span class="price sold">ausverkauft</span>
%end