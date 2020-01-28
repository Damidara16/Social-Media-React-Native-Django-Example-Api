import * as React from 'react';
import { Text, View, StyleSheet,Button, TouchableOpacity, TextInput, Image, ImageBackground, SafeAreaView, ScrollView, FlatList } from 'react-native';
import Ionicon from 'react-native-vector-icons/Ionicons';



//like button needs it own function

const DATA = {}
const BORDER = 20;

Imagee = () => {
  return (
    <View style={{flexDirection:'row', height:450, width:'100%'}}>
      <View style={{backgroundColor:'', flex:1, alignItems:'center', paddingTop:20, paddingStart:10}}>
        <Ionicon name='ios-heart-empty' size={30} />
        <Text style={{paddingBottom:10}}>20</Text>
        <Ionicon  name='ios-chatboxes' size={30} />
        <Text style={{paddingBottom:10}}>20</Text>
        <Ionicon style={{paddingBottom:15}} name='ios-send' size={30} />
        <Ionicon name='ios-bookmark' size={30} />
        <Ionicon style={{bottom:10, right:0, position:'absolute'}} name='ios-more' size={30} />
      </View>

      <View style={{backgroundColor:'', flex:10, justifyContent:'center', alignItems:'center'}}>
        <TouchableOpacity style={{height:'97%', width:'90%', backgroundColor:'green',alignItems:'center', borderRadius:BORDER}}>
          <ImageBackground style={{justifyContent:'center', alignItems:'center',height:'100%', width:'100%', overflow:'hidden', borderRadius:BORDER}} source={{uri:'https://static.boredpanda.com/blog/wp-content/uploads/2014/12/Top-10-photographers-for-travel-portraits27__700.jpg'}}>
          </ImageBackground>
          <View style={{flexDirection:'row',alignItems:'center',height:60, width:'94%', backgroundColor:'pink', position:'absolute', bottom:10, borderRadius:30}}>
            <TouchableOpacity style={{flex:1, backgroundColor:''}}>
              <Image style={{width:40, height:40, borderRadius:20, marginLeft:10}} source={{uri:'https://specials-images.forbesimg.com/imageserve/5d70b0225b52ce0008826162/960x0.jpg'}}/>
            </TouchableOpacity>
            <View style={{flex:4,height:'100%', paddingRight:10,backgroundColor:'', paddingTop:5, paddingStart:5}}>
              <Text style={{fontWeight:'700'}}>Jenny Poster * 4 mins ago</Text>
              <TouchableOpacity><Text numberOfLines={2}>An interesting live application. It's a cool thing to play a game with a anchor while watching live.</Text></TouchableOpacity>
            </View>
          </View>
        </TouchableOpacity>
      </View>
    </View>
  );
}

QPoste = () => {
  return (
    <View style={{flexDirection:'row',alignItems:'center',height:75, width:'94%', backgroundColor:'pink',  marginStart:12, borderRadius:30}}>
      <TouchableOpacity style={{flex:1, backgroundColor:''}}>
        <Image style={{width:50, height:50, borderRadius:25, marginLeft:10}} source={{uri:'https://specials-images.forbesimg.com/imageserve/5d70b0225b52ce0008826162/960x0.jpg'}}/>
      </TouchableOpacity>
      <View style={{flex:6,height:'100%', paddingRight:10,backgroundColor:'', paddingTop:5, paddingStart:5, marginLeft:20}}>
        <Text style={{fontWeight:'700', fontSize:15}}>Jenny Poster * 4 mins ago</Text>
        <TouchableOpacity><Text style={{fontSize:12}} numberOfLines={2}>An interesting live application. It's a cool thing to play a game with a anchor while watching live.</Text></TouchableOpacity>
      </View>
      <View style={{flex:1}}>
      <Ionicon name='ios-heart-empty' size={35}/>
      </View>
    </View>

  )
}


export default class DiscoverTabScreen extends React.Component {

  constructor(props){
    super(props);
  }

  APIAction = () => {
    fetch('http://127.0.0.1:8000/account/auth/',{method:'post',headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body:JSON.stringify({})}).then(res=>res.json()).then(res=>{console.log(res)})
  }

  componentDidMount(){
    console.log('discover');
  }


  render() {
    return (
      <SafeAreaView style={{flex:1,backgroundColor:'#eeebeb'}}>
      <View style={{height:50,width:'100%', backgroundColor:'#ebebeb', justifyContent:'center',alignItems:'center'}}>
      <Text style={{fontSize:26,fontWeight:'700'}}>FanMojis</Text>
      </View>
<ScrollView>



<Imagee/>
<Imagee url=''/>
<Imagee url=''/>
<QPoste/>
<Imagee url=''/>
<QPoste/>
<Imagee url=''/>
<QPoste/>


</ScrollView>
      </SafeAreaView>

    );
  }
}


const styles = StyleSheet.create({

});
