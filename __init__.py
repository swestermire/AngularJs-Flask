from flask import Flask

# from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
# from sqlalchemy import create_engine, asc
# from sqlalchemy.orm import sessionmaker
# from database_setup import Base, Restaurant, MenuItems
# from flask import session as login_session
# import random
# import string

# # IMPORTS FOR THIS STEP
# from oauth2client.client import flow_from_clientsecrets
# from oauth2client.client import FlowExchangeError, AccessTokenCredentials
# import httplib2
# import json
# from flask import make_response
# import requests

app = Flask(__name__)

# if it were in another file, it would be "filename.app_routes"
import app_routes


# Connect to Database and create database session

# @app.route('/login')
# def showLogin():
#     state = ''.join(random.choice(string.ascii_uppercase + string.digits)
#                     for x in range(32))
#     login_session['state'] = state
#     # return "The current session state is %s" % login_session['state']
#     return render_template('login.html', STATE=state)

# #this is a callback method to handle google response
# @app.route('/gconnect', methods=['POST'])
# def gconnect():
#     # Validate state token
#     if request.args.get('state') != login_session['state']:
#         response = make_response(json.dumps('Invalid state parameter.'), 401)
#         response.headers['Content-Type'] = 'application/json'
#         return response
#     # Obtain authorization code
#     code = request.data

#     try:
#         # Upgrade the authorization code into a credentials object
#         oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
#         oauth_flow.redirect_uri = 'postmessage'
#         credentials = oauth_flow.step2_exchange(code)
#     except FlowExchangeError:
#         response = make_response(
#             json.dumps('Failed to upgrade the authorization code.'), 401)
#         response.headers['Content-Type'] = 'application/json'
#         return response

#     # Check that the access token is valid.
#     access_token = credentials.access_token
#     url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
#            % access_token)
#     h = httplib2.Http()
#     result = json.loads(h.request(url, 'GET')[1])
#     # If there was an error in the access token info, abort.
#     if result.get('error') is not None:
#         response = make_response(json.dumps(result.get('error')), 500)
#         response.headers['Content-Type'] = 'application/json'
#         return response

#     # Verify that the access token is used for the intended user.
#     gplus_id = credentials.id_token['sub']
#     if result['user_id'] != gplus_id:
#         response = make_response(
#             json.dumps("Token's user ID doesn't match given user ID."), 401)
#         response.headers['Content-Type'] = 'application/json'
#         return response

#     # Verify that the access token is valid for this app.
#     if result['issued_to'] != CLIENT_ID:
#         response = make_response(
#             json.dumps("Token's client ID does not match app's."), 401)
#         print( "Token's client ID does not match app's.")
#         response.headers['Content-Type'] = 'application/json'
#         return response

#     stored_credentials = login_session.get('credentials')
#     stored_gplus_id = login_session.get('gplus_id')
#     if stored_credentials is not None and gplus_id == stored_gplus_id:
#         response = make_response(json.dumps('Current user is already connected.'),
#                                  200)
#         response.headers['Content-Type'] = 'application/json'
#         return response

#     # Store the access token in the session for later use.
#     login_session['credentials'] = credentials.access_token
#     login_session['gplus_id'] = gplus_id

#     # Get user info
#     userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
#     params = {'access_token': credentials.access_token, 'alt': 'json'}
#     answer = requests.get(userinfo_url, params=params)

#     data = answer.json()

#     login_session['username'] = data['name']
#     login_session['picture'] = data['picture']
#     login_session['email'] = data['email']

#     output = ''
#     output += '<h1>Welcome, '
#     output += login_session['username']
#     output += '!</h1>'
#     output += '<img src="'
#     output += login_session['picture']
#     output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
#     flash("you are now logged in as %s" % login_session['username'])
#     return output


# # JSON APIs to view Restaurant Information
# @app.route('/restaurant/<int:restaurant_id>/menu/JSON')
# def restaurantMenuJSON(restaurant_id):
#     restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
#     items = session.query(MenuItem).filter_by(
#         restaurant_id=restaurant_id).all()
#     return jsonify(MenuItems=[i.serialize for i in items])


# @app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/JSON')
# def menuItemJSON(restaurant_id, menu_id):
#     Menu_Item = session.query(MenuItems).filter_by(id=menu_id).one()
#     return jsonify(Menu_Item=Menu_Item.serialize)


# @app.route('/restaurant/JSON')
# def restaurantsJSON():
#     restaurants = session.query(Restaurant).all()
#     return jsonify(restaurants=[r.serialize for r in restaurants])


# # Show all restaurants
# @app.route('/')
# @app.route('/restaurant/')
# def showRestaurants():
#     restaurants = session.query(Restaurant).order_by(asc(Restaurant.name))
#     return render_template('restaurants.html', restaurants=restaurants)

# # Create a new restaurant


# @app.route('/restaurant/new/', methods=['GET', 'POST'])
# def newRestaurant():
#     if request.method == 'POST':
#         newRestaurant = Restaurant(name=request.form['name'])
#         session.add(newRestaurant)
#         flash('New Restaurant %s Successfully Created' % newRestaurant.name)
#         session.commit()
#         return redirect(url_for('showRestaurants'))
#     else:
#         return render_template('newRestaurant.html')

# # Edit a restaurant


# @app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
# def editRestaurant(restaurant_id):
#     editedRestaurant = session.query(
#         Restaurant).filter_by(id=restaurant_id).one()
#     if request.method == 'POST':
#         if request.form['name']:
#             editedRestaurant.name = request.form['name']
#             flash('Restaurant Successfully Edited %s' % editedRestaurant.name)
#             return redirect(url_for('showRestaurants'))
#     else:
#         return render_template('editRestaurant.html', restaurant=editedRestaurant)


# # Delete a restaurant
# @app.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
# def deleteRestaurant(restaurant_id):
#     restaurantToDelete = session.query(
#         Restaurant).filter_by(id=restaurant_id).one()

#     if request.method == 'POST':
#         session.delete(restaurantToDelete)
#         flash('%s Successfully Deleted' % restaurantToDelete.name)
#         session.commit()
#         return redirect(url_for('showRestaurants', restaurant_id=restaurant_id))
#     else:
#         return render_template('deleteRestaurant.html', restaurant=restaurantToDelete)

# # Show a restaurant menu


# @app.route('/restaurant/<int:restaurant_id>/')
# @app.route('/restaurant/<int:restaurant_id>/menu/')
# def showMenu(restaurant_id):
#     restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
#     items = session.query(MenuItems).filter_by(
#         restaurant_id=restaurant_id).all()
#     return render_template('menu.html', items=items, restaurant=restaurant)


# # Create a new menu item
# @app.route('/restaurant/<int:restaurant_id>/menu/new/', methods=['GET', 'POST'])
# def newMenuItem(restaurant_id):
#     restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
#     if request.method == 'POST':
#         newItem = MenuItems(name=request.form['name'], restaurant_id=restaurant_id)
#         session.add(newItem)
#         session.commit()
#         flash('New Menu %s Item Successfully Created' % (newItem.name))
#         return redirect(url_for('showMenu', restaurant_id=restaurant_id))
#     else:
#         return render_template('newmenuitem.html', restaurant_id=restaurant_id)

# # Edit a menu item


# @app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit', methods=['GET', 'POST'])
# def editMenuItem(restaurant_id, menu_id):

#     editedItem = session.query(MenuItems).filter_by(id=menu_id).one()
#     restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
#     if request.method == 'POST':
#         if request.form['name']:
#             editedItem.name = request.form['name']
#         if request.form["description"]:
#             editedItem.description = request.form['description']
#         if request.form["price"]:
#             editedItem.price = request.form['price']
#         session.add(editedItem)
#         session.commit()
#         flash('Menu Item Successfully Edited')
#         return redirect(url_for('showMenu', restaurant_id=restaurant.id))
#     else:
#         return render_template('editmenuitem.html', restaurant=restaurant, menu_item=editedItem, item=editedItem)


# # Delete a menu item
# @app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete', methods=['GET', 'POST'])
# def deleteMenuItem(restaurant_id, menu_id):
#     restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
#     itemToDelete = session.query(MenuItems).filter_by(id=menu_id).one()
    
#     if request.method == 'POST':
#         session.delete(itemToDelete)
#         session.commit()
#         flash('Menu Item Successfully Deleted')
#         return redirect(url_for('showMenu', restaurant_id=restaurant.id))
#     else:
#         return render_template('deleteMenuItem.html', restaurant = restaurant , menuItem=itemToDelete)


# @app.route('/gdisconnect')
# def gdisconnect():
#     #Only disconnects a connected users
#     credientials = login_session('credentials')
#     if credentials is None:
#         response = make_response(json.dumps('Current user is not connected'),
#             401)
#         response.headers['Content-Type'] = 'application/json'
#         return response
#     access_token = credientials.access_token
#     url = 'https://accounts.google.com/o/auth2/revoke?token=%s' % access_token
#     h = httplib2.Http()
#     result = h.request(url, 'GET')[0]

#     if result['status'] == '200':
#         #reset the user's session
#         del login_session['credentials']
#         del login_session['gplus_id']
#         del login_session['username']
#         del login_session['email']
#         del login_session['picture']

#         response= make_response(json.dumps("Successfuly disconnected..."), 200)
#         response.headers['Content-Type'] = 'application/json'
#         return response

#     else:
#         #for whatever reason this coudl fail, the given token was invalid maybe.
#         response = make_response(json.dumps("Failed to revoke token from given user."), 400)
#         response.headers['Content-Type'] = 'application/json'
#         return response