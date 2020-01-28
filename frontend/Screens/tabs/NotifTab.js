import * as React from 'react';
import { Text, View, StyleSheet,Button, TouchableOpacity, TextInput, ScrollView, Image,StatusBar, SafeAreaView, Picker, FlatList } from 'react-native';
import QPost from '../../content/QPostComp';
import ContentHeader from '../../comp/content_header';
import ContentFooter from '../../comp/content_footer';
import displayDate from '../../app_funcs';
import AntDesign from 'react-native-vector-icons/AntDesign';
import MaterialCommunityIcons from 'react-native-vector-icons/MaterialCommunityIcons';
import Ionicon from 'react-native-vector-icons/Ionicons';
//import NFooter from '../../comp/content_nfooter'

const TOKEN = '933d66153aec6d5b205eab69174300bd27ca415d'

FlatListItemSeparator = () => {
  return (
    <View
      style={{
        height: 10
      }}
    ></View>
  );
}

export default class NotifTabScreen extends React.Component {
  constructor(props){
    super(props);
    this.state = {comment:false};
    this.data;
  }

  APIAction = () => {
    fetch('http://127.0.0.1:8000/feed/notif/',{method:'get',headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      'Authorization': 'Token ' + TOKEN
    }}).then(res=>res.json()).then(res=>{
      if (res['outcome'] !== 'success'){
        console.log('error');
      } else {
        this.data=res.data;
        this.setState({});

        //this.forceUpdate();

      }
    })
  }

  componentDidMount(){
    console.log('notif')
  }


  render() {
    const HEIGHT = 40;
    const COLOR = '#eeebeb';
    const BLOCK = 15;
    return (
      <SafeAreaView style={{flex:1,backgroundColor:COLOR}}>
      <ScrollView>
      <View style={{height:50,width:'100%', backgroundColor:'#ebebeb', justifyContent:'center',alignItems:'center'}}>
      <Text style={{fontSize:26,fontWeight:'700'}}>FanMojis</Text>
      </View>
        <View style={{height:BLOCK}}></View>

        <View style={{flex:1,justifyContent:'center',alignItems:'center'}}>
          <TouchableOpacity style={{height:450, width:'95%'}}><Image style={{height:'100%', width:'100%', overflow:'hidden',borderTopRightRadius:15, borderTopLeftRadius:15}} source={{uri:'https://www.destinsparks.com/wp-content/uploads/2017/03/tips-for-better-selfies.jpg'}}/>
          </TouchableOpacity>
          <ContentFooter c={true}/>


          <View style={{height:BLOCK}}></View>
          <TouchableOpacity style={{height:300, width:'95%'}}><Image style={{height:'100%', width:'100%', overflow:'hidden',borderTopRightRadius:15, borderTopLeftRadius:15}} source={{uri:'https://s24193.pcdn.co/wp-content/uploads/2018/06/Screen-Shot-2018-06-25-at-3.43.31-PM.png'}}/>
          </TouchableOpacity>
          <ContentFooter/>

          <View style={{height:BLOCK}}></View>
          <TouchableOpacity style={{height:400, width:'95%'}}><Image style={{height:'100%', width:'100%', overflow:'hidden',borderTopRightRadius:15, borderTopLeftRadius:15}} source={{uri:'https://www.essence.com/wp-content/uploads/2019/06/selfie-hero-1920x1080.jpg?width=1920&height=1080'}}/>
          </TouchableOpacity>
          <ContentFooter c={true}/>

          <View style={{height:BLOCK}}></View>
          <ContentFooter qp={true} c={true}/>

          <View style={{height:BLOCK}}></View>
          <TouchableOpacity style={{height:250, width:'95%'}}><Image style={{height:'100%', width:'100%', overflow:'hidden',borderTopRightRadius:15, borderTopLeftRadius:15}} source={{uri:'https://static.boredpanda.com/blog/wp-content/uploads/2019/12/funny-moms-selfies-people-responses-2.jpg'}}/>
          </TouchableOpacity>
          <ContentFooter h={75}/>

          <View style={{height:BLOCK}}></View>
          <ContentFooter qp={true} c={true}/>

          <View style={{height:BLOCK}}></View>
          <ContentFooter qp={true} c={true}/>

          <View style={{height:BLOCK}}></View>
          <TouchableOpacity style={{height:400, width:'95%'}}><Image style={{height:'100%', width:'100%', overflow:'hidden',borderTopRightRadius:15, borderTopLeftRadius:15}} source={{uri:'https://hudabeauty.com/wp-content/uploads/2017/04/perfect-selfie-apps.jpg'}}/>
          </TouchableOpacity>
          <ContentFooter/>

        </View>
      </ScrollView>
      </SafeAreaView>
    );
  }
}


{/*
        <FlatList
    data={this.data}
    keyExtractor={item => item.cuuid}
    ListHeaderComponent={
        <View style={{height:50,width:'100%', backgroundColor:'#ebebeb', justifyContent:'center',alignItems:'center'}}>
        <Text style={{fontSize:26,fontWeight:'700'}}>Notifications</Text>
        </View>
      }
    ItemSeparatorComponent = { FlatListItemSeparator }
    renderItem={({ item }) => {
      switch (item.type) {
       case 'post':
         return <Poster uuid={item.cuuid}/>
         break;
       case 'qpost':
         return <QPost uuid={item.cuuid}/>
         break;
       case 'image':
          return <Imager uuid={item.cuuid}/>

         break;


     }}}


        />*/}


const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginTop: 10,
  },
  item: {
    backgroundColor: '#f9c2ff',
    padding: 20,
    marginVertical: 8,
    marginHorizontal: 16,
  },
  title: {
    fontSize: 32,
  },
});
