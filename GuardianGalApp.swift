import SwiftUI

@main
struct GuardianGalApp: App {
    var body: some Scene {
        WindowGroup {
            HomeScreen()
            
        }
    }
}

struct HomeScreen: View {
    var body: some View {
        VStack {
            Spacer()
            Text("Welcome to GuardianGal")
                .font(.title)
                .foregroundColor(.blue)
            Spacer()

            Button(action: {
                            runPythonScript1()
                        }) {
                            Label("Excuse", systemImage: "play.circle")
                        }
            
            NavigationLink(destination: SMSView()) {
                Button(action: {
                                runPythonScript2()
                            }) {
                                Label("SMS", systemImage: "play.circle")
                            }
            }

            NavigationLink(destination: VoiceAIView()) {
                Button(action: {
                                runPythonScript3()
                            }) {
                                Label("Voice AI", systemImage: "play.circle")
                            }
            }
            
            Spacer()
        }
    
    }
}

func runPythonScript1() {
        let process = Process()
        process.launchPath = "/Library/Frameworks/Python.framework/Versions/3.12/bin/python3"
        process.arguments = ["/Applications/pyth/callCode.py"]
        process.launch()

    }

func runPythonScript2() {
        let process = Process()
        process.launchPath = "/Library/Frameworks/Python.framework/Versions/3.12/bin/python3"
        process.arguments = ["/Applications/pyth/sms.py"]
        process.launch()

    }

func runPythonScript3() {
        let process = Process()
        process.launchPath = "/Library/Frameworks/Python.framework/Versions/3.12/bin/python3"
        process.arguments = ["/Applications/pyth/ai.py"]
        process.launch()

    }

struct HomeScreen_Previews: PreviewProvider {
    static var previews: some View {
        HomeScreen()
    }
}



