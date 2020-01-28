import * as React from 'react';
import { Text, View, StyleSheet, Image, TouchableOpacity, Button, SafeAreaView } from 'react-native';
import ContentHeader from './comp/content_header';
import ContentFooter from './comp/content_footer';
import { createBottomTabNavigator } from 'react-navigation-tabs';
import { createAppContainer, createSwitchNavigator } from 'react-navigation';
import {createStackNavigator } from 'react-navigation-stack';
import Ionicon from 'react-native-vector-icons/Ionicons';

import PreLoginScreen from './Screens/PreLogin';
import ProfileEditScreen from './Screens/ProfileEdit';
import SignUpScreen from './Screens/SignUp';
import LoginScreen from './Screens/Login';

import CreateTabScreen from './Screens/tabs/CreateCTab';
import HomeTabScreen from './Screens/tabs/HomeTab';
import NotifTabScreen from './Screens/tabs/NotifTab';
import ProfileTabScreen from './Screens/tabs/ProfileTab';
import ChatTabScreen from './Screens/tabs/ChatTab';




const TOKEN = '7af9cf0939d69dd0ed37e06a18c188f347f012f7'

const appStack = createBottomTabNavigator({
    Feed1:{
      screen:HomeTabScreen,
      navigationOptions:{
          tabBarIcon:()=><Ionicon name='ios-home' size={20} color='#84828F'/>}
    },
    Feed2:{
      screen:ChatTabScreen,
      navigationOptions:{
          tabBarIcon:()=><Ionicon name='ios-paper' size={20} color='#84828F'/>}
    },

    Feed3:{
      screen:NotifTabScreen,
      navigationOptions:{
          title:'Alerts',
          tabBarIcon:()=><Ionicon name='ios-filing' size={20} color='#84828F'/>}
    }

},
{
  defaultNavigationOptions:{
  tabBarOptions: {
          activeTintColor: 'red',
          labelStyle: {fontSize: 12},
          style:{backgroundColor:'#eeebeb'}
          }
        }
},
);
const rootStack = createSwitchNavigator({
  App:appStack,
  Pre:PreLoginScreen,
  Login:LoginScreen,
  SignUp:createStackNavigator({signup:SignUpScreen, profile:ProfileEditScreen},{defaultNavigationOptions:{headerShown:false}})

  },

  {
    initialRouteName: 'Pre',
  });

const AppContainer = createAppContainer(appStack);

export default class App extends React.Component {
  render() {
    return (
      <AppContainer/>
    );
  }
}
