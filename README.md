# SKP Sync to Blender


este script precisa do Addon Sketchup Importer para Funcionar

Download em: https://github.com/RedHaloStudio/Sketchup_Importer/releases



Abra um novo arquivo do blender e salve o na mesma pasta e com o mesmo nome do arquivo do sketchup.

Execute o script, ele deve sincronizar a primeira ver e criar um loop que verifica o arquivo .skp a cada segundo para alterações.

se tiver problemas, abra o console do Blender no menu 'Window/Toggle System Console' e aperte Ctrl+c algumas vezes. depois disso tente executar o script novamente.

Nunca coloque nada dentro da Collection "Sketchup" pois a cada atualização será removido.

## TODO

- Documentar o Codigo
- Implementar este script como Addon para o Blender
- Implementar um Plugin para o Sketchup que apartir de um botão automaticamente cria o arquivo blender se necessário, abre o blender e importa o SKP.
- Encontrar uma solução usando  SDK do Sketchup para fazer exportações realtime.