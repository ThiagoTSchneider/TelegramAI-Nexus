# 🤖 Bot de Telegram com GPT-3.5-turbo e Eleven Labs

## Descrição

Este é um projeto de bot para o Telegram que utiliza duas APIs poderosas para proporcionar interações inteligentes, gerando respostas de texto e áudio de maneira autônoma.

## Funcionalidades Principais

1. **Respostas de Texto com GPT-3.5-turbo:**
   - 🧠 O bot utiliza a API da OpenAI e o modelo GPT-3.5-turbo para gerar respostas de texto de maneira natural, com base nas mensagens recebidas dos usuários.

2. **Geração de Áudio com Eleven Labs:**
   - 🔊 Além das respostas em texto, o bot é capaz de gerar áudio com base nas interações dos usuários. Esta funcionalidade é alcançada através da API da Eleven Labs.

3. **Segurança das Chaves de API:**
   - 🔐 As chaves de API necessárias para acessar as funcionalidades da OpenAI e Eleven Labs são mantidas de forma segura usando variáveis de ambiente, garantindo a proteção das informações sensíveis.

## Configuração

Antes de executar o código, é necessário configurar suas chaves de API como variáveis de ambiente no sistema operacional. Certifique-se de substituir `<Sua Chave da Eleven Labs>`, `<Sua Chave da OpenAI>`, e `<Sua Chave do Telegram>` pelos valores reais.

```bash
export ELEVENLABS_KEY='<Sua Chave da Eleven Labs>'
export OPENAI_KEY='<Sua Chave da OpenAI>'
export TELEGRAM_KEY='<Sua Chave do Telegram>'
```
Contribuições
Contribuições para o projeto são bem-vindas! 🙌 Sinta-se à vontade para abrir problemas ou enviar solicitações de pull. Se você tiver alguma sugestão ou correção, ficaremos felizes em ouvir!

Contato

GitHub: @ThiagoTSchneider
E-mail: thiagottschneider@gmail.com
