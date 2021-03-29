import { useNavigation } from '@react-navigation/native';
import React from 'react';
import { Button, Image, ImageBackground, StyleSheet, Text, View } from 'react-native';
import { Tooltip } from 'react-native-elements';

import Menu from '../../components/Menu'


const image = require('../../assets/home.png');
const miles = require('../../assets/miles.png')

const Home = () => (
  <View style={styles.container}>
    <Menu />
    <ImageBackground source={image} style={styles.image}>
        <View style={styles.textbox}>
            <Text style={styles.textMiles}>Olá, me chamo Miles e sou sua Personal Travel. Vamos começar a planejar sua viagem dos sonhos?</Text>
        </View>
        <Image source={miles} style={styles.miles} />
    </ImageBackground>
  </View>
);

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: "column"
  },
  textbox:{
    flex: 0.2,
    marginTop: '70%',
    marginHorizontal: '20%',
    backgroundColor: '#FFF',
    borderBottomLeftRadius: 15,
    borderTopLeftRadius: 15,
    borderTopRightRadius: 15,
  },
  textMiles: {
    paddingVertical: 10,
    paddingHorizontal: 20,
    color: '#E48040'
  },
  image: {
    flex: 1,
    resizeMode: "cover",
    justifyContent: "center"
  },
  miles: {
    position: 'absolute',
    top: '75%',
    alignSelf: 'flex-end',
    color: "white",
    fontWeight: "bold",
    textAlign: "center",
  }
});


export default Home;