## adding in new pages that show up in the side menu

# add routes to:
cleanui/src/router.js
# add pages to:
cleanui/src/pages/dashboard
    -> TODO: function to generate links based on list
# add page links to menu
cleanui/src/services/menu
    -> TODO: function to generate links based on list

------------------------------------------------------------------------

## general src schema

# assets
->

# components schema
        -> cleanui components
        -> layout components
        -> site specific

# layouts schema
        -> Login
        -> Main
        -> Public

# locales schema
-> just insert languages that you can support here

# pages schema
        -> client (login passed)
        -> dashboard (regular)
            --> place login option on top
                -> main
                -> gallery
                -> about
                -> contact us

        -> login (forogt, login)
        -> 404

# redux schema (https://redux.js.org/basics/reducers)
    -> menu
        -> actions.js (Actions are payloads of information that send data from your application to your store)
        -> reducer.js (Reducers specify how the application's state changes in response to actions sent to the store. Describes what not how!)
        -> sagas.js (the redux middleware: https://redux-saga.js.org/)
    -> settings
        ->actions.js / reducer.js / sagas.js
    -> user
        ->actions.js / reducer.js / sagas.js

    -> reducers.js
    -> sagas.js

# services schema
    -> menu (functions: get_left_menu && get_top_menu)

    -> user (asynchronous functions: login, currentAccount, logout)

# other files
-> global.scss (imports for css styling: https://responsivedesign.is/articles/difference-between-sass-and-scss/)
-> index.js (setup of store, middleware, logging, and language format for localization)
-> router.js (all available routes for the website)
-> serviceWorker.js (fuctions: register(if in right location), ... not too sure about this stuff)
-> theme.js (general theme settings and colors etc)



------------------------------------------------------------------------
##general app schema

# Public
    -> resouces (pictures, fonts, images)
    -> index.js (basic picture that shows client that javascript must be enabled to view page)
    -> manifest.js ()
