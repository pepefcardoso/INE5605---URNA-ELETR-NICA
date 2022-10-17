# O presente trabalho foi desenvolvido pelos alunos Pedro Paulo Fernandes Cardoso e Daniel Sottovia Gomide durante a matéria
Desenvolvimento de Sistemas Orientados a Objetos (INE5605) do curso de Sistemas de Informação da UFSC.

# O objetivo é implementar um sistema orientado a objetos em Python para simulação de uma urna eletrônica
para votação em reitor e pró-reitores.

# Escopo de Desenvolvimento: Em uma eleição da UFSC, cada centro possui uma urna eleitoral. Cada urna eleitoral deve ser
configurada para um determinado turno (primeiro ou segundo) de uma eleição, bem como
devem constar na urna os candidatos inscritos para os cargos de reitor e pró-reitores. Cada
candidato concorre para um determinado cargo (reitor ou pró-reitor), sendo filiado a uma
determinada chapa.
A urna estando homologada, no dia da realização de votação, o voto pode ser realizado. Cada
eleitor deverá votar em um reitor e um pró-reitor para cada pró-reitoria (Graduação, Pesquisa e
Extensão). Considere que a urna deve ser configurada para aceitar uma quantidade configurável
de eleitores e candidatos. A lista completa dos votos deve ser guardada na urna.
Existem três grupos de eleitores: professores, técnicos administrativos e alunos.
Encerrada a votação, a urna totaliza os votos válidos (por candidato para cada cargo) e os votos
inválidos (brancos e nulos). Além disso, o sistema deve totalizar quais foram os candidatos eleitos
para cada cargo.

# Restrições de Escopo: Para simplificar este trabalho, o sistema contempla somente algumas das funcionalidades de
uma urna eletrônica, não abordando todas as questões de segurança, criptografia e
funcionalidades do sistema do mesário, por exemplo.
