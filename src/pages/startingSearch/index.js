import { useNavigation } from '@react-navigation/native';
import React from 'react';
import { Button, Image, ImageBackground, StyleSheet, Text, TextInput, View } from 'react-native';
import { RectButton } from 'react-native-gesture-handler';
import Menu from '../../components/Menu'


const StartingSearch = () => {

    const navigation = useNavigation();

    function handleNavigateToPoints() {
        navigation.navigate('Points');
    }

    function handleNavigateToRegister() {
        navigation.navigate('Register');
    }
    
    function handleNavigateToBack() {
        navigation.goBack();
    }

    return (
        <>
            <View style={styles.container}>
                <Menu />
                <View style={styles.section}>
                    <View style={styles.textContainer}>
                        <Text style={styles.title}>
                        Quando geralmente você costuma viajar?
                        </Text>
                        <TextInput style={styles.input} placeholder="Digite seu texto aqui"/>
                    </View>
                    <View style={styles.buttonContainer}>
                        <RectButton style={styles.button}>
                            <Text style={styles.buttonText}>Iniciar</Text>
                        </RectButton>
                    </View>
                </View>
                <View style={styles.footer}>
                    <Image style={styles.img} source={require('../../../assets/miles2.png')} />
                </View>
            </View>
        </>

    );

}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
    },

    menu: {
        flex: 1,
        marginTop: 40,
    },
    section: {
        flex: 3,
        justifyContent: 'center',
        alignItems: 'center',
        paddingTop: 30,
        margin: 15,
    },
    box: {
        backgroundColor: '#28407C',
        width: '100%',
        height: 20,
        borderTopEndRadius: 15,
        borderTopStartRadius: 15,
    },

    textContainer: {
        flex: 1,
        width: 500,
        justifyContent: 'center',
        alignItems: 'center'
    },
    buttonContainer: {
        flex: 0.3,
        width: 500,
        justifyContent: 'center',
        alignItems: 'baseline',
        maxWidth: 260,
    },
    buttonText: {
        color:'#e48040',
    },


    title: {
        flex: 1,
        textAlign: 'center',
        color: '#515151',
        fontSize: 20,
        fontFamily: 'Roboto_500Medium',
        textAlign: 'left',
        maxWidth: 260,
        marginTop: 25
    },
    input:{
        flex: 1,
        textAlign: 'center',
        width: '100%',
        color: '#AEAEAE',
        fontSize: 14,
        fontFamily: 'Roboto_400Regular',
        maxWidth: 300,
        backgroundColor: 'red'
    },

    text: {
        flex: 3,
        textAlign: 'center',
        width: '100%',
        color: '#AEAEAE',
        fontSize: 14,
        fontFamily: 'Roboto_400Regular',
        maxWidth: 300,
        backgroundColor: 'red'
    },

    description: {
        color: '#6C6C80',
        fontSize: 16,
        marginTop: 16,
        fontFamily: 'Roboto_400Regular',
        maxWidth: 260,
        lineHeight: 24,
    },

    footer: {
        flex: 3,
        alignItems: 'center'
    },

    img: {
        width:250,
        height:300,
    },
    background: {
        backgroundColor: '#0E0E0E',
    },

    button: {
        justifyContent: 'center',
       
        height: 60,
        width: 150,
        flexDirection: 'row',
        alignItems: 'center',
        marginTop: 20,
    },
    buttonText: {
        flex: 1,
        justifyContent: 'center',
        textAlign: 'center',
        borderWidth:1,
        borderStyle: 'solid',
        borderColor:'#e48040',
        color: '#e48040',
        fontFamily: 'Roboto_500Medium',
        fontSize: 14,
        margin:5,
    }
});

export default StartingSearch;
