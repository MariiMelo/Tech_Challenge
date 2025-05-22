
# Tech Challenge: Previsão do Preço do Petróleo Brent 

Este projeto foi desenvolvido como parte do Tech Challenge da pós-graduação em Data & Analytics (FIAP).

# LINK PARA O VÍDEO: https://www.loom.com/share/f426a2afb4c54bb58e354d4de1f0c5ff?sid=95363d10-c368-40ab-9c31-6732f7e01ecf

##  Objetivo
Construir um modelo de Machine Learning que preveja o preço do petróleo Brent com base em dados históricos, e entregar isso por meio de uma aplicação interativa.

##  Tecnologias e ferramentas
- Python
- Pandas
- Prophet (Facebook)
- Matplotlib
- Scikit-learn
- Streamlit

##  Funcionalidades do App (Streamlit)
- Upload de arquivo CSV com dados históricos
- Previsão dos próximos 30 dias (e também 365 dias)
- Gráficos da previsão
- Cálculo automático de MAE e RMSE

##  Deploy
Você pode acessar o app aqui: https://techchallenge-petroleoprices.streamlit.app/

##  Como usar
1. Faça upload de um arquivo CSV com as colunas `Date` e `Preço (USD)`
2. O app irá treinar o modelo Prophet e mostrar as previsões
3. As métricas de erro serão exibidas na tela

## Fonte dos dados
Os dados utilizados foram obtidos da [IPEA DATA](http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view).

---

