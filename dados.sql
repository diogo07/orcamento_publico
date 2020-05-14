insert into funcao_despesa (codigo, tipo) values(1, 'Legislativa'),
												(2, 'Judiciaria'),
												(3, 'Essencial à Justiça'),
												(4, 'Administração'),
												(5, 'Defesa Nacional'),
												(6, 'Segurança Pública'),
												(7, 'Relações Exteriores'),
												(8, 'Assistencia Social'),
												(9, 'Previdencia Social'),
												(10, 'Saúde'),
												(11, 'Trabalho'),
												(12, 'Educação'),
												(13, 'Cultura'),
												(14, 'Direitos a Cidadania'),
												(15, 'Urbanismo'),
												(16, 'Habitação'),
												(17, 'Saneamento'),
												(18, 'Gestão Ambiental'),
												(19, 'Ciência e Tecnologia'),
												(20, 'Agricultura'),
												(21, 'Organização Agrária'),
												(22, 'Mineração'),
												(23, 'Comércio e Serviços'),
												(24, 'Comunicações'),
												(25, 'Energia'),
												(26, 'Transporte)'),
												(27, 'Desporto e Lazer'),
												(28, 'Encargos Especiais'),
												(29, 'Outras Despesas');
												
insert into funcao_receita (codigo, tipo) values(1, 'Receitas Correntes'),
												(2, 'Receitas de Capital'),
												(7, 'Receitas Correntes - Intraorçamentárias'),
												(8, 'Receitas de Capital - Intraorçamentárias');
												
												
insert into classificacao_receita (codigo, tipo) values (1, 'Deduções - FUNDEB'), 
							(2, 'Deduções - Transferências Constitucionais'),
							(3, 'Outras Deduções da Receita'),
							(4, 'Receitas Brutas Realizadas');


insert into classificacao_despesa (codigo, tipo) values	(1, 'Despesas Empenhadas'), 
							(2, 'Despesas Liquidadas'), 
							(3, 'Despesas Pagas'), 
							(4, 'Inscrição de Restos a Pagar Não Processados'), 
							(5, 'Inscrição de Restos a Pagar Processados');

