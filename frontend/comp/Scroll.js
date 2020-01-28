import * as React from 'react';
import { Text, View, StyleSheet,Button, TouchableOpacity, TextInput, ScrollView, Image } from 'react-native';
import Constants from 'expo-constants';

// You can import from local files
import { MaterialCommunityIcons, AntDesign } from '@expo/vector-icons';
import Imager from '../content/ImageComp';
import Tweeter from '../content/TweetComp';
import Poster from '../content/PostComp';

export default class Scroller extends React.Component {
  constructor(props) {
  super(props);
  }
  render(){
    return(
    <ScrollView style={{width:'100%'}}>
        <Imager/>
        <View style={{height:10}}></View>
        <Poster/>
        <View style={{height:10}}></View>
        <Imager/>
        <View style={{height:10}}></View>
        <Imager/>
        <View style={{height:10}}></View>
        <Imager/>
        <View style={{height:10}}></View>
        <Tweeter/>
        <View style={{height:10}}></View>
        <Imager/>
        <View style={{height:10}}></View>
        <Tweeter/>
        <View style={{height:10}}></View>
        <Imager/>
        <View style={{height:10}}></View>
        <Poster/>
        <View style={{height:10}}></View>
        <Imager/>
        <View style={{height:10}}></View>
        <Poster/>
        <View style={{height:10}}></View>
        <Imager/>
        <View style={{height:10}}></View>
        <Imager/>
        <View style={{height:10}}></View>
        <Imager/>
        <View style={{height:10}}></View>
        <Tweeter/>
        <View style={{height:10}}></View>
        <Imager/>
        <View style={{height:10}}></View>
        <Tweeter/>
        <View style={{height:10}}></View>
        <Imager/>
        <View style={{height:10}}></View>
        <Poster/>
        <View style={{height:10}}></View>
      </ScrollView>
    );
  }
}
