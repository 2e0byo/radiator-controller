# [1.3.0](https://github.com/2e0byo/esp8266-radiator-controller/compare/v1.2.1...v1.3.0) (2022-11-27)


### Bug Fixes

* cleanup. ([6c17ea4](https://github.com/2e0byo/esp8266-radiator-controller/commit/6c17ea451796e829298879b8089f8811398fabaa))
* save fs space. ([67abf01](https://github.com/2e0byo/esp8266-radiator-controller/commit/67abf01c443df8d3abfefcae52d53e389ad83306))
* **sensor:** handle implicit bad sensor which returns None. ([9ffec51](https://github.com/2e0byo/esp8266-radiator-controller/commit/9ffec516fe4cda3a429bb2b834156bd26a2dac25))


### Features

* graph. ([5c5b1e5](https://github.com/2e0byo/esp8266-radiator-controller/commit/5c5b1e5f1c1f7f453e9690eaa3860fa6da292594))
* Sensor() class and tests. ([5baa2be](https://github.com/2e0byo/esp8266-radiator-controller/commit/5baa2be26e827019b438cd42a116bf3c6ac683c4))
* wdt. ([37ab380](https://github.com/2e0byo/esp8266-radiator-controller/commit/37ab3805940a2abe7cf3721cd6fe64886cd24bcc))

## [1.2.1](https://github.com/2e0byo/esp8266-radiator-controller/compare/v1.2.0...v1.2.1) (2022-04-09)


### Bug Fixes

* **cleanup:** remove empty dirs which otherwise suppress real code! ([79aa296](https://github.com/2e0byo/esp8266-radiator-controller/commit/79aa296a548cc6a8bcfc749dd9a33ebb421b9149))
* **clock:** work against utc, and handle rounding. ([d2aea99](https://github.com/2e0byo/esp8266-radiator-controller/commit/d2aea990cdbfa7eedf4cc426a87528aeedff9586))

# [1.2.0](https://github.com/2e0byo/esp8266-radiator-controller/compare/v1.1.0...v1.2.0) (2022-04-04)


### Bug Fixes

* **clock:** fix localtime endpoint. ([905dba8](https://github.com/2e0byo/esp8266-radiator-controller/commit/905dba8f6ce6442429336dc62dd4bb89ec82f438))
* **clock:** offset in hours! ([46569ac](https://github.com/2e0byo/esp8266-radiator-controller/commit/46569acd41ed74635baab39455dbd25f69d25efb))
* **clock:** use uurequests, but not in event loop as it dies! ([2ed5d6b](https://github.com/2e0byo/esp8266-radiator-controller/commit/2ed5d6be479ec5e9fcae258eb3a38e92f6ba1370))
* **scheduler:** avoid appending rule multiple times. ([695ecaa](https://github.com/2e0byo/esp8266-radiator-controller/commit/695ecaa8c1e70ca3674adddb682ee02adb602acd))
* **scheduler:** handle single once off rules properly. ([0c17a54](https://github.com/2e0byo/esp8266-radiator-controller/commit/0c17a54dbd98f219990e88c951c1a9f30df80be6))
* **scheduler:** toggle on `Scheduler()` to know state. ([110de06](https://github.com/2e0byo/esp8266-radiator-controller/commit/110de065319c52839766dc0df26eebaf48f54a2a))


### Features

* **clock:** localtime endpoint. ([16685f3](https://github.com/2e0byo/esp8266-radiator-controller/commit/16685f32120c00b59e234fe57d40b2512a44f2eb))
* **clock:** set timezone. ([170b527](https://github.com/2e0byo/esp8266-radiator-controller/commit/170b527d90f8b0be5be7d04f424e9349233e9cf1))
* **clock:** set uptime on boot. ([006d58c](https://github.com/2e0byo/esp8266-radiator-controller/commit/006d58cb6b31029704c19bdcf20a2d53145f177a))
* **clock:** start syncing when connected. ([6cb9099](https://github.com/2e0byo/esp8266-radiator-controller/commit/6cb909973e2953aed5caf31ca6ffd4dedc02d479))
* **scheduler/api:** use remove_by_id. ([4ae66f4](https://github.com/2e0byo/esp8266-radiator-controller/commit/4ae66f43e124a35f096605ba13469f596aae6b12))
* **scheduler:** better repr. ([a43b601](https://github.com/2e0byo/esp8266-radiator-controller/commit/a43b6016ff3fd559ed46bfeeb2bd2c4be76bdd34))
* **scheduler:** justify api. ([b5d0127](https://github.com/2e0byo/esp8266-radiator-controller/commit/b5d0127434bcf6d2e81415b73791fda55e96476a))
* **scheduler:** justify fn. ([e6163bd](https://github.com/2e0byo/esp8266-radiator-controller/commit/e6163bde5bdc2c719fe1e8b0b44e1196411a9f24))
* **scheduler:** remove_by_id. ([df4b049](https://github.com/2e0byo/esp8266-radiator-controller/commit/df4b0490cd762458a0cc6d7537df7be00fef912b))

# [1.1.0](https://github.com/2e0byo/esp8266-radiator-controller/compare/v1.0.0...v1.1.0) (2022-01-14)


### Features

* **api:** clock api. ([0db88c1](https://github.com/2e0byo/esp8266-radiator-controller/commit/0db88c1ef42b5f171f5a55bdec3005db69c705c0))
* **api:** settings api. ([db893ce](https://github.com/2e0byo/esp8266-radiator-controller/commit/db893ce8d95b7142786ceb114a73b8bf1f169154))
* **scheduler/api:** once off api. ([7d00fe2](https://github.com/2e0byo/esp8266-radiator-controller/commit/7d00fe23f4da5c63dc4115a5ef952ca193b2ed9a))
* **scheduler:** duration now in minutes and on the rule. ([63ca21e](https://github.com/2e0byo/esp8266-radiator-controller/commit/63ca21e59f4d62f5649f3873a9f832abcb5739a4))
* **scheduler:** make api more helpful. ([c8af531](https://github.com/2e0byo/esp8266-radiator-controller/commit/c8af5316f46138283938b404b8ad997da1d0fae5))

# 1.0.0 (2022-01-14)


### Bug Fixes

* **api:** general fixups and typos. ([54986a6](https://github.com/2e0byo/esp8266-radiator-controller/commit/54986a61644b1a5b43865e7f844756a905016e40))
* **api:** typo. ([52d43a2](https://github.com/2e0byo/esp8266-radiator-controller/commit/52d43a238488161de03e42ef83cb056395f42f80))
* **clock:** log needs str. ([1fa55c6](https://github.com/2e0byo/esp8266-radiator-controller/commit/1fa55c67bec1e12ba86aeb5aefb856855538e79d))
* **log:** move logging init to log and fixup. ([007e386](https://github.com/2e0byo/esp8266-radiator-controller/commit/007e386397a0a9082e67d1c8cb4621fd426ae03f))
* **log:** prevent \n from mucking up linewise log. ([11b1354](https://github.com/2e0byo/esp8266-radiator-controller/commit/11b135432fef84dc32738628b189963be0d1a7e4))
* **main:** set root handler. ([dd4af08](https://github.com/2e0byo/esp8266-radiator-controller/commit/dd4af08990a78f936bbe6c5eaf9b11388c660397))
* **radiator:** imports from hal. ([2233aec](https://github.com/2e0byo/esp8266-radiator-controller/commit/2233aeca1b957b0823e5cb116ee3ba2ae0a3d50d))
* **scheduler:** api fixup. ([9548060](https://github.com/2e0byo/esp8266-radiator-controller/commit/95480607aca27b7b78167123934bb9af10d1605e))
* **scheduler:** correct and simplify logic. ([8ba2f82](https://github.com/2e0byo/esp8266-radiator-controller/commit/8ba2f828b2da6edd7f75bfde45a52c4680fc0348))
* **scheduler:** fix delay_ms invocation. ([6acc147](https://github.com/2e0byo/esp8266-radiator-controller/commit/6acc1472d168417c96602dc171a08b6ac0673d6e))
* **scheduler:** fix load/save. ([2d52fec](https://github.com/2e0byo/esp8266-radiator-controller/commit/2d52fecff1ee2f2277cc3df304763c706333442f))
* **scheduler:** gate for empty cases. ([fd64b52](https://github.com/2e0byo/esp8266-radiator-controller/commit/fd64b529b6e4a29c7d091f5ceaae306fa2bcae63))
* **scheduler:** get running. ([546c1a2](https://github.com/2e0byo/esp8266-radiator-controller/commit/546c1a2705322d190ce2e8e8008f48db505be608))
* **scheduler:** next_event only calculates when told to. ([34db6ca](https://github.com/2e0byo/esp8266-radiator-controller/commit/34db6ca461224c17ca4c0f4052df39a0d007cd8d))
* **scheduler:** timediff. ([dc8a478](https://github.com/2e0byo/esp8266-radiator-controller/commit/dc8a478b5c56c432ea6e4706ff87bbeea019ab7e))
* **scheduler:** typo ([0bcc058](https://github.com/2e0byo/esp8266-radiator-controller/commit/0bcc0587729fb78d511b4eb8bfd0ee5ee613059b))
* **scheduler:** typo. ([802b192](https://github.com/2e0byo/esp8266-radiator-controller/commit/802b192f28a325d0fe73574bd9b580cb00e06cad))
* **scheduler:** use to_json in load/save correctly. ([68e9685](https://github.com/2e0byo/esp8266-radiator-controller/commit/68e9685d2aaad4f03b2e743ff57ca6c543e671dc))
* try to reduce ram with gc. ([5cd9244](https://github.com/2e0byo/esp8266-radiator-controller/commit/5cd924433dc223673e82c3af247fe253a6621330))


### Features

* add once_off ([4166e77](https://github.com/2e0byo/esp8266-radiator-controller/commit/4166e77452e5027e15459716beef873789240daf))
* api. ([839262d](https://github.com/2e0byo/esp8266-radiator-controller/commit/839262d549f9bcf737f3c8053ce2298ec23adf9c))
* **api:** catchall. ([db629c4](https://github.com/2e0byo/esp8266-radiator-controller/commit/db629c45c559710587951d28ad217c65dbf148f9))
* **api:** consistent persistence. ([1a60129](https://github.com/2e0byo/esp8266-radiator-controller/commit/1a60129ae6be5a0d257e4113d3aabbb8928eceec))
* **api:** move to radiator and use dict. ([ee780bd](https://github.com/2e0byo/esp8266-radiator-controller/commit/ee780bdc087d0be54dd8e4ab8f429d4527d59579))
* **api:** standardise endpoints ([f258bf5](https://github.com/2e0byo/esp8266-radiator-controller/commit/f258bf52db0cbdfe2a51f2b26937f3385f88d354))
* **api:** static files. ([3db65fa](https://github.com/2e0byo/esp8266-radiator-controller/commit/3db65fa37d4505a259133b6f9e5bcea0eef23d3b))
* **api:** use to_json(). ([4523266](https://github.com/2e0byo/esp8266-radiator-controller/commit/452326640b3270122fd07e5d5cce2bd09a35ec5b))
* **app:** add next endpoint. ([34c5aa6](https://github.com/2e0byo/esp8266-radiator-controller/commit/34c5aa60548a06d829c70edf071d21f074e4a571))
* **app:** get radiator on time from settings. ([1e6ead3](https://github.com/2e0byo/esp8266-radiator-controller/commit/1e6ead36d43f404d95d3afd03e5925595b226b73))
* **app:** haptic with sound not light. ([ecfbfbb](https://github.com/2e0byo/esp8266-radiator-controller/commit/ecfbfbb3503372cda5e4155446d10fb00a758497))
* **app:** in debug mode. ([f25f2a3](https://github.com/2e0byo/esp8266-radiator-controller/commit/f25f2a3a30c41828cef84f7131df86668d515871))
* **app:** new entrypoint. ([f9e9d44](https://github.com/2e0byo/esp8266-radiator-controller/commit/f9e9d449aacd0df28d51b216fc8d13e7c4247a3d))
* **app:** set up as before. ([8a11764](https://github.com/2e0byo/esp8266-radiator-controller/commit/8a11764ea250108dbee02362271242452e101d7f))
* basic arch. ([631b9c3](https://github.com/2e0byo/esp8266-radiator-controller/commit/631b9c323f39d5ba8052ff731f9121e861cfca53))
* clock. ([81f7196](https://github.com/2e0byo/esp8266-radiator-controller/commit/81f7196a65c07ab81391fcf9f36f4448e5f7094f))
* **datetimematch:** prevent infinite loop with malicious input. ([07ee580](https://github.com/2e0byo/esp8266-radiator-controller/commit/07ee580e6c80d83820866650da709ef494ef9d21))
* **hal:** drop cumbersome radiator. ([68ef96d](https://github.com/2e0byo/esp8266-radiator-controller/commit/68ef96d59da6ae03014450c997d7258ef1d6b955))
* **hal:** finish hal ([57cb43e](https://github.com/2e0byo/esp8266-radiator-controller/commit/57cb43e10d1d1aff56f354c7f9f0dde7e31e5829))
* **hal:** noisy pin. ([e7004fc](https://github.com/2e0byo/esp8266-radiator-controller/commit/e7004fc5087457ec0af6ea7e70e8ec1bb05c3a77))
* heartbeat for debugging. ([732770e](https://github.com/2e0byo/esp8266-radiator-controller/commit/732770eb7fc8b26098a7f20b11cc4022104eb0b2))
* log.py ([54f8275](https://github.com/2e0byo/esp8266-radiator-controller/commit/54f8275cd154dfc41564df9fcd1ef82835d5e1b2))
* **log:** add api. ([e669fe8](https://github.com/2e0byo/esp8266-radiator-controller/commit/e669fe8c16100f638dd9c03e06394cdd1b8f2ef1))
* **main:** gc. ([909c62d](https://github.com/2e0byo/esp8266-radiator-controller/commit/909c62d2ef791a2cee6ba53067e7168ab93c1b62))
* **main:** sync clock. ([862fef3](https://github.com/2e0byo/esp8266-radiator-controller/commit/862fef3945dbba1f3bba0b31389c12d9019fe1b0))
* remove other scheduler ([c9654dd](https://github.com/2e0byo/esp8266-radiator-controller/commit/c9654dd74dcf2577a88b7a5860a89442cfefc766))
* **rule:** add id to json. ([30f1f00](https://github.com/2e0byo/esp8266-radiator-controller/commit/30f1f0009b479db89a783297b3228b103bf9969c))
* scheduler ([a605882](https://github.com/2e0byo/esp8266-radiator-controller/commit/a6058827c977b64d2d623fef719461622f6f72d7))
* **scheduler:** add id. ([94650cc](https://github.com/2e0byo/esp8266-radiator-controller/commit/94650cca7b9469dc69581e6b85dc3f72feb1f5b5))
* **scheduler:** append/remove. ([8308cb2](https://github.com/2e0byo/esp8266-radiator-controller/commit/8308cb29fb3a468da1986671a078b93f7b58d97d))
* **scheduler:** be more human readable. ([af0d0ed](https://github.com/2e0byo/esp8266-radiator-controller/commit/af0d0edd4d5c4a26cc65081cc028a08a359cf94a))
* **scheduler:** be verbose about using mock. ([affa21d](https://github.com/2e0byo/esp8266-radiator-controller/commit/affa21df1466ffdd2fb3d17f9ca5285c9fbe1f59))
* **scheduler:** handle exceptions when loading. ([8da5f22](https://github.com/2e0byo/esp8266-radiator-controller/commit/8da5f22b74a69f8c504748f4bcea6fba65e095bb))
* **scheduler:** json once_off. ([25bf02b](https://github.com/2e0byo/esp8266-radiator-controller/commit/25bf02bcb5698b326e2a0e2756b4413dea9a9663))
* **scheduler:** optional duration, otherwise taken from rule. ([c8bac9b](https://github.com/2e0byo/esp8266-radiator-controller/commit/c8bac9ba07e8adc0eb4c2db0194f2345bede3815))
* **scheduler:** rules json serialisable. ([0c2a4e0](https://github.com/2e0byo/esp8266-radiator-controller/commit/0c2a4e00257bf13054630b13d57f259b65cc4e89))
* **scheduler:** rules list api. ([ee62944](https://github.com/2e0byo/esp8266-radiator-controller/commit/ee629445ee91499e0f9862d9a769fe03af62f28f))
* **scheduler:** rules property. ([723e162](https://github.com/2e0byo/esp8266-radiator-controller/commit/723e162454f2b829ef10393cccafc6326b2bb514))
* settings.py ([029eae2](https://github.com/2e0byo/esp8266-radiator-controller/commit/029eae2aa86e6b74228a0f4b95e567f1857ab497))
