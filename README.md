# ROS Nedir?

<b>ROS</b>, (Robot Operating System - Robot İşletim Sistemi) robotlar için, açık kaynak bir meta işletim sistemidir. Bir işletim sisteminden yapması beklenen donanım soyutlaması, düşük seviye aygıt kontrolü, yaygın kullanılan fonksiyonelliğin uygulanması, işllemler arası mesaj geçisi ve paket yönetimi gibi servisleri sağlar. Ayrıca kodun, çoklu bilgisayarlar arasında temin edilmesi, derlenmesi, yazılması ve çalıştırılması için araç ve kütüphaneler sağlar. Bazı yönlerden, Player, YARP, Orocos, CARMEN, Orca, MOOS ve Microsoft Robotics Studio gibi robot frameworklerine benzer.

# Workspace Nedir? Nasıl Oluşturulur?

<b>Workspace</b>, (çalışma alanı) ROS kodunun içinde bulunduğu, bu kodla ilişkili klasörler kümesidir. Bir bilgisayarda birden çok ROS çalışma alanına sahip olunabilir fakat aynı anda bunlardan yalnızca biriyle çalışılabilir. 

<b>Catkin</b>, ROS için derleme sistemidir. ROS'un çalıştırılabilir programlar, kütüphaneler, komut dosyaları ve diğer kodların kullanabileceği arayüzler oluşturmak için kullandığı araç kümesidir. Normal CMake iş akışının üzerine ekstra fonksiyonellik sağlayan CMake makrolarının bir kümesi ve özel Python komut dosyalarından oluşur.

#### Workspace Nasıl Oluşturulur?

<b>Catkin çalışma alanı</b>, catkin paketlerinin değiştirildiği, derlendiği ve yüklendiği bir klasördür. Tavsiye edilen ve tipik catkin çalışma alanı düzeni şöyledir:

    
```sh
workspace_folder/         -- WORKSPACE
  src/                    -- SOURCE SPACE
    CMakeLists.txt        -- The 'toplevel' CMake file
    package_1/
      CMakeLists.txt
      package.xml
      ...
    package_n/
      CATKIN_IGNORE       -- Optional empty file to exclude package_n from being processed
      CMakeLists.txt
      package.xml
      ...
  build/                  -- BUILD SPACE
    CATKIN_IGNORE         -- Keeps catkin from walking this directory
  devel/                  -- DEVELOPMENT SPACE (set by CATKIN_DEVEL_PREFIX)
    bin/
    etc/
    include/
    lib/
    share/
    .catkin
    env.bash
    setup.bash
    setup.sh
    ...
  install/                -- INSTALL SPACE (set by CMAKE_INSTALL_PREFIX)
    bin/
    etc/
    include/
    lib/
    share/
    .catkin             
    env.bash
    setup.bash
    setup.sh
    ...
```

<b>Catkin çalışma alanı</b> şu komutlarla oluşturulur ve derlenir:

```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
```

Bu komutlar ilk kez çalıştırıldığında 'src' klasörünün içinde CMakeLists.txt dosyası oluşturulur. Ayrıca, mevcut çalışma alanında 'build' ve 'devel' isimli iki klasör oluşturulur. 'devel' klasörünün içinde birkaç setup.*sh dosyaları bulunur. Aşağıdaki komut ile bu çalışma alanı ROS ortamının üzerine bindirilir:

```
source ~/catkin_ws/devel/setup.bash
```

Aşağıdaki komut ile bu komut .bashrc dosyasına eklenir.

```
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
```

Çalışma alanının doğru bir şekilde ortamın üzerine bindirildiğinden emin olmak için ROS_PACKAGE_PATH ortamının çalışma alanının olduğu klasörü içermesi beklenir. Bunun için şu komut yazılır:

```
echo $ROS_PACKAGE_PATH
```

Komutun döndürmesi beklenen sonuç şudur:

```
/home/<username>/catkin_ws/src:/opt/ros/kinetic/share
```

# ROS Node Nedir?

<b>Node</b>, (düğüm) ROS'ta hesaplama yapan bir işlemdir. Basit olarak, ROS paketi içindeki çalıştırılabilir bir dosyadır. Bu düğümler akış topic'leri, RPC servisleri ve parametre sunucusu kullanarak birbirleriyle haberleşirler.
Bir robot kontrol sistemi genellikle birçok düğümden meydana gelir. Örneğin; lazer mesafe ölçeri kontrol eden düğüm, robotun tekerlek motorlarını kontrol eden düğüm vs.

Bu <b>düğüm</b>ler hakkındaki bilgileri görüntülemek için `rosnode` komutu kullanılır. Bu komut info, kill, list gibi parametreler alır.